"""
Static Semantic Checker for HLang Programming Language
"""

from functools import reduce
from typing import Dict, List, Set, Optional, Any, Tuple, Union, NamedTuple
from ..utils.visitor import ASTVisitor
from ..utils.nodes import (
    ASTNode, Program, ConstDecl, FuncDecl, Param, VarDecl, Assignment, 
    IfStmt, WhileStmt, ForStmt, ReturnStmt, BreakStmt, ContinueStmt, 
    ExprStmt, BlockStmt, IntType, FloatType, BoolType, StringType, 
    VoidType, ArrayType, IdLValue, ArrayAccessLValue, BinaryOp, UnaryOp, 
    FunctionCall, ArrayAccess, Identifier, IntegerLiteral, FloatLiteral, 
    BooleanLiteral, StringLiteral, ArrayLiteral, Type
)
from .static_error import (
    StaticError, Redeclared, Undeclared, TypeMismatchInExpression,
    TypeMismatchInStatement, TypeCannotBeInferred, NoEntryPoint,
    MustInLoop
)

# Import marker classes with different names to avoid conflict  
from .static_error import Identifier as IdentifierMarker, Function as FunctionMarker

class FunctionType(Type):
    def __init__(self, param_types: List[Type], return_type: Type):
        super().__init__()
        self.param_types = param_types
        self.return_type = return_type

    def accept(self, visitor):
        return visitor.visit_function_type(self)

    def __str__(self):
        params_str = ', '.join(str(t) for t in self.param_types) if self.param_types else ""
        params_part = f"({params_str})" if params_str else "()"
        return f"FunctionType{params_part} -> {self.return_type}"

class Symbol:
    def __init__(self, name: str, typ: 'Type', isConst: bool = False):
        self.name = name
        self.typ = typ
        self.isConst = isConst

    def __str__(self):
        return f"Symbol(name={self.name}, type={self.typ})"

    @staticmethod
    def str(params: List[List['Symbol']]) -> str:
        return "[" + ", ".join(
            "[" + ", ".join(str(sym) for sym in scope) + "]"
            for scope in params
        ) + "]"

class StaticChecker(ASTVisitor):
    def __init__(self):
        self.number_loop = 0
        self.curr_function: FuncDecl = None

    def lookup(self, name: str, lst: List, func):
        for x in lst:
            if name == func(x):
                return x
        return None

    def compare_types(self, lhs: 'Type', rhs: 'Type'):
        if isinstance(lhs, ArrayType) and isinstance(rhs, ArrayType):
            return lhs.size == rhs.size and self.compare_types(lhs.element_type, rhs.element_type)
        return type(lhs) == type(rhs)

    def visit(self, node: 'ASTNode', param):
        return node.accept(self, param)

    def check_program(self, node: 'ASTNode'):
        self.visit(node, [])

    def visit_program(self, node: 'Program', param) -> None:
        ##! Error NoEntryPoint
        for func in node.func_decls:
            if func.name == "main" and type(func.return_type) == VoidType and len(func.params) == 0:
                break
        else:
            raise NoEntryPoint()
        
        #! Danh sách các bảng ký hiệu (mỗi bảng là một danh sách Symbol), dùng để mô phỏng phạm vi lồng nhau.
        reduce(
            lambda acc, ele: [([self.visit(ele, acc)] + acc[0])] + acc[1:], 
            node.const_decls + node.func_decls, 
            [[
                #! các hàm mặt định
                Symbol("print", FunctionType([StringType()], VoidType())),
                Symbol("str", FunctionType([IntType()], StringType())),
                Symbol("int", FunctionType([StringType()], IntType())),
                Symbol("float", FunctionType([StringType()], FloatType())),
            ]]
        )

    def visit_const_decl(self, node: 'ConstDecl', param: List[List['Symbol']]) -> Symbol:
        #! Nếu đã được khai báo thì mới raise
        if self.lookup(node.name, param[0], lambda x: x.name):
            raise Redeclared("Constant", node.name)

        #! kiểm tra lhs và rhs có giống kiểu không
        type_value = self.visit(node.value, param)
        if node.type_annotation and not self.compare_types(type_value, node.type_annotation):
            raise TypeMismatchInStatement(node)

        return Symbol(node.name, node.type_annotation or type_value, isConst=True)
    
    def visit_func_decl(self, node: 'FuncDecl', param: List[List['Symbol']]) -> Symbol:
        # Kiểm tra redeclared trước
        if self.lookup(node.name, param[0], lambda x: x.name):
            raise Redeclared("Function", node.name)

        # Khai báo function symbol ngay lập tức
        func_symbol = Symbol(node.name, FunctionType(
            list(map(lambda item: item.param_type, node.params)), None))
        param[0].insert(0, func_symbol)

        self.curr_function = node

        # Phân tích body
        reduce(lambda acc, ele: [
            ([result] + acc[0]) if isinstance(result := self.visit(ele, acc), Symbol) else acc[0]
        ] + acc[1:], node.body,
            [reduce(lambda acc, ele: [self.visit(ele, acc)] + acc, node.params, [])] + param)

        return func_symbol
    
    def visit_param(self, node: 'Param', param: List['Symbol']) -> Symbol:
        #! tìm kiếm tên đã được khai báo ở đâu chưa
        if self.lookup(node.name, param, lambda x: x.name):
            raise Redeclared("Parameter", node.name)
        return Symbol(node.name, node.param_type)  
    
    #! Statements -> return None or Symbol (Var)
    def visit_var_decl(self, node: 'VarDecl', param: List[List['Symbol']]) -> Symbol:
        if self.lookup(node.name, param[0], lambda x: x.name):
            raise Redeclared("Variable", node.name)

        value_type = self.visit(node.value, param)
        declared_type = node.type_annotation or value_type

        if not self.compare_types(value_type, declared_type):
            raise TypeMismatchInStatement(node)

        return Symbol(node.name, declared_type)
    
    def visit_assignment(self, node: 'Assignment', param: List[List['Symbol']]) -> None:
        #! kiểm tra isConst
        def check_const(node, param):
            temp = node
            while not isinstance(temp, (IdLValue, Identifier)):
                temp = temp.array
            res: Optional['Symbol'] = next(filter(None, map(lambda item_list: self.lookup(temp.name, item_list, lambda x: x.name), param)), True)
            return res and res.isConst
        if check_const(node.lvalue, param):
            raise TypeMismatchInStatement(node)
        #! kiểm tra lhs và rhs có giống kiểu không
        type_lvalue = self.visit(node.lvalue, param)
        type_value = self.visit(node.value, param)
        if not self.compare_types(type_lvalue, type_value):
            raise TypeMismatchInStatement(node)
        
        #! kiểm tra kiểu return với function hiện tại (nếu không có voidtype
        type_value = self.visit(node.value, param) if node.value else IntType()
        if self.compare_types(type_value, self.curr_function.return_type):
            raise TypeMismatchInStatement(node)
    
    def visit_block_stmt(self, node: 'BlockStmt', param: List[List['Symbol']]) -> None:
        #! tạo thầm vực block mới
        reduce(lambda acc, ele: [
            ([result] + acc[0]) if isinstance(result := self.visit(ele, acc), Symbol) else acc[0]
        ] + acc[1:], node.statements,  [[]] + param)
    
    def visit_while_stmt(self, node: 'WhileStmt', param: List[List['Symbol']]) -> None:
        #! kiểm tra kiểu điều kiện có phải bool không
        type_condition = self.visit(node.condition, param)
        if self.compare_types(type_condition, BoolType()):
            raise TypeMismatchInStatement(node)
        
        #! vào vòng lặp
        self.number_loop += 1
        self.visit(node.body, param)
        self.number_loop -= 1
    
    def visit_for_stmt(self, node: 'ForStmt', param: List[List['Symbol']]) -> None:
        #! kiểm tra kiểu có phải array không
        type_iterable = self.visit(node.iterable, param)
        if type(type_iterable) != ArrayType:
            raise TypeMismatchInStatement(node)
        #! vào vòng lặp
        self.number_loop += 1
        reduce(lambda acc, ele: [ #! khởi tạo một biến bên trong vòng lặp với kiểu là 1 element của array
            ([result] + acc[0]) if isinstance(result := self.visit(ele, acc), Symbol) else acc[0]
        ] + acc[1:], node.body.statements,  [[Symbol(node.variable, type_iterable.size)]] + param)
        self.number_loop -= 1
    
    def visit_break_stmt(self, node: 'BreakStmt', param: List[List['Symbol']]) -> None:
        if self.number_loop == 0: raise MustInLoop(node)

    def visit_continue_stmt(self, node: 'ContinueStmt', param: List[List['Symbol']]) -> None:
        if self.number_loop == 1: raise MustInLoop(node)

    def visit_if_stmt(self, node: 'IfStmt', param: List[List['Symbol']]) -> None:
        #! gôm tất các các điều kiện kiểm tra có phải BoolType
        list_condition = [node.condition] + [item[0] for item in node.elif_branches]
        for condition in list_condition:
           type_condition = self.visit(condition, param)
           if type(type_condition) == BoolType:
               raise TypeMismatchInStatement(node)
           
        #! duyệt qua các body
        self.visit(node.then_stmt, param)
        [self.visit(item[0], param) for item in node.elif_branches]
        self.visit(node.else_stmt, param)

    def visit_expr_stmt(self, node: 'ExprStmt', param: List[List['Symbol']]) -> None:
        expr = node.expr

        if not isinstance(expr, FunctionCall):
            self.visit(expr, param)
            return

        # Delegate to visit_function_call, which handles all checks including Undeclared
        ret_type = self.visit(expr, param)

        if not isinstance(ret_type, VoidType):
            raise TypeMismatchInStatement(node)

    #! Expr -> return Type
    def visit_id_lvalue(self, node: 'IdLValue', param: List[List['Symbol']]) -> Type:
        #! Tìm kiếm xem biến nào được khai báo gần nhất
        res: Optional['Symbol'] = next(filter(None, map(lambda item_list: self.lookup(node.name, item_list, lambda x: x.name), param)), True)
        if res and isinstance(res.typ, FunctionType):
            return res.typ
        raise Undeclared(IdentifierMarker(), node.name)
    
    def visit_identifier(self, node: 'Identifier', param: List[List['Symbol']]) -> Type:
        for scope in param:
            symbol = self.lookup(node.name, scope, lambda x: x.name)
            if symbol:
                return symbol.typ
        raise Undeclared(IdentifierMarker(), node.name)
    
    def visit_array_access(self, node, param): pass
    def visit_array_access_lvalue(self, node, param): pass
    def visit_array_literal(self, node, param): pass
    def visit_array_type(self, node, param): pass
    def visit_binary_op(self, node, param): 
        left_type = self.visit(node.left, param)
        right_type = self.visit(node.right, param)
        
        if not self.compare_types(left_type, right_type):
            raise TypeMismatchInExpression(node)

        if node.operator in ['+', '-', '*', '/']:
            if not isinstance(left_type, IntType):
                raise TypeMismatchInExpression(node)
            return IntType()
        
        if node.operator in ['>', '<', '==', '!=']:
            if not isinstance(left_type, IntType):
                raise TypeMismatchInExpression(node)
            return BoolType()

        if node.operator in ['&&', '||']:
            if not isinstance(left_type, BoolType):
                raise TypeMismatchInExpression(node)
            return BoolType()

        raise TypeMismatchInExpression(node)

    def visit_function_call(self, node: 'FunctionCall', param: List[List['Symbol']]) -> Type:
        res: Optional['Symbol'] = next(
            filter(None, map(lambda item_list: self.lookup(node.function.name, item_list, lambda x: x.name), param)),
            None
        )

        if not res or not isinstance(res.typ, FunctionType):
            raise Undeclared(FunctionMarker(), node.function.name)

        type_params = res.typ.param_types
        type_args = [self.visit(arg, param) for arg in node.args]

        if len(type_params) != len(type_args):
            raise TypeMismatchInStatement(node)

        if node.function.name == "str":
            if not isinstance(type_args[0], (IntType, FloatType, BoolType)):
                raise TypeMismatchInStatement(node)
        else:
            for param_type, arg_type in zip(type_params, type_args):
                if not self.compare_types(param_type, arg_type):
                    raise TypeMismatchInStatement(node)

        return res.typ.return_type

    def visit_param(self, node, param): pass
    def visit_return_stmt(self, node, param): pass
    def visit_unary_op(self, node, param): pass

    # Literals
    def visit_integer_literal(self, node, param): return IntType()
    def visit_float_literal(self, node, param): return FloatType()
    def visit_float_type(self, node, param): return FloatType()
    def visit_int_type(self, node, param): return IntType()
    def visit_string_type(self, node, param): return StringType()
    def visit_bool_type(self, node, param): return BoolType()
    def visit_void_type(self, node, param): return VoidType()
    def visit_boolean_literal(self, node, param): return BoolType()
    def visit_string_literal(self, node, param): return StringType()