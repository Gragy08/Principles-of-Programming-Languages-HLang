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
        for func in node.func_decls:
            if func.name == "main" and type(func.return_type) == VoidType and len(func.params) == 0:
                break
        else:
            raise NoEntryPoint()
        
        reduce(
            lambda acc, ele: [([self.visit(ele, acc)] + acc[0])] + acc[1:], 
            node.const_decls + node.func_decls, 
            [[
                Symbol("print", FunctionType([StringType()], VoidType())),
                Symbol("str", FunctionType([IntType()], StringType())),
                Symbol("int", FunctionType([StringType()], IntType())),
                Symbol("float", FunctionType([StringType()], FloatType())),
                Symbol("input", FunctionType([], StringType())),
            ]]
        )

    def visit_const_decl(self, node: 'ConstDecl', param: List[List['Symbol']]) -> Symbol:
        if self.lookup(node.name, param[0], lambda x: x.name):
            raise Redeclared("Constant", node.name)

        type_value = self.visit(node.value, param)
        if node.type_annotation and not self.compare_types(type_value, node.type_annotation):
            raise TypeMismatchInStatement(node)

        return Symbol(node.name, node.type_annotation or type_value, isConst=True)
    
    def visit_func_decl(self, node: 'FuncDecl', param: List[List['Symbol']]) -> Symbol:
        if self.lookup(node.name, param[0], lambda x: x.name):
            raise Redeclared("Function", node.name)

        func_symbol = Symbol(node.name, FunctionType(
            list(map(lambda item: item.param_type, node.params)), node.return_type))
        param[0].insert(0, func_symbol)

        self.curr_function = node

        reduce(lambda acc, ele: [
            ([result] + acc[0]) if isinstance(result := self.visit(ele, acc), Symbol) else acc[0]
        ] + acc[1:], node.body,
            [reduce(lambda acc, ele: [self.visit(ele, acc)] + acc, node.params, [])] + param)

        return func_symbol
    
    def visit_param(self, node: 'Param', param: List['Symbol']) -> Symbol:
        if self.lookup(node.name, param, lambda x: x.name):
            raise Redeclared("Parameter", node.name)
        return Symbol(node.name, node.param_type, isConst=True)  
    
    def visit_var_decl(self, node: 'VarDecl', param: List[List['Symbol']]) -> Symbol:
        if self.lookup(node.name, param[0], lambda x: x.name):
            raise Redeclared("Variable", node.name)
        value_type = self.visit(node.value, param)
        if isinstance(value_type, VoidType):
            raise TypeMismatchInExpression(node.value)
        declared_type = node.type_annotation or value_type
        if not self.compare_types(value_type, declared_type):
            raise TypeMismatchInStatement(node)
        sym = Symbol(node.name, declared_type)
        param[0].insert(0, sym)
        return sym
    
    def visit_assignment(self, node: 'Assignment', param: List[List['Symbol']]) -> None:
        def check_const_and_declared(lvalue, param):
            temp = lvalue
            while not isinstance(temp, (IdLValue, Identifier)):
                temp = temp.array
            
            def is_var_symbol(sym: Symbol):
                return not isinstance(sym.typ, FunctionType)

            res: Optional['Symbol'] = next(
                filter(None, map(lambda item_list: self.lookup(
                    temp.name, item_list, lambda x: x.name if is_var_symbol(x) else None
                ), param)),
                None
            )

            if res is None:
                raise Undeclared(IdentifierMarker(), temp.name)
            return res.isConst

        if check_const_and_declared(node.lvalue, param):
            raise TypeMismatchInStatement(node)

        type_lvalue = self.visit(node.lvalue, param)
        type_value = self.visit(node.value, param)
        if not self.compare_types(type_lvalue, type_value):
            raise TypeMismatchInStatement(node)

        if self.curr_function and self.curr_function.return_type:
            if self.compare_types(type_value, self.curr_function.return_type):
                raise TypeMismatchInStatement(node)
    
    def visit_block_stmt(self, node: 'BlockStmt', param: List[List['Symbol']]) -> None:
        new_scope = []
        new_param = [new_scope] + param
        last_error = None

        for stmt in node.statements:
            try:
                result = self.visit(stmt, new_param)
                if isinstance(result, Symbol):
                    new_scope.append(result)
            except StaticError as e:
                last_error = e

        if last_error:
            raise last_error
    
    def visit_while_stmt(self, node: 'WhileStmt', param: List[List['Symbol']]) -> None:
        type_condition = self.visit(node.condition, param)
        if not self.compare_types(type_condition, BoolType()):
            raise TypeMismatchInStatement(node)
        
        self.number_loop += 1
        self.visit(node.body, param)
        self.number_loop -= 1
    
    def visit_for_stmt(self, node: 'ForStmt', param: List[List['Symbol']]) -> None:
        type_iterable = self.visit(node.iterable, param)
        if type(type_iterable) != ArrayType:
            raise TypeMismatchInStatement(node)
        self.number_loop += 1
        reduce(lambda acc, ele: [
            ([result] + acc[0]) if isinstance(result := self.visit(ele, acc), Symbol) else acc[0]
        ] + acc[1:], node.body.statements,  [[Symbol(node.variable, type_iterable.element_type)]] + param)
        self.number_loop -= 1
    
    def visit_break_stmt(self, node: 'BreakStmt', param: List[List['Symbol']]) -> None:
        if self.number_loop == 0: raise MustInLoop(node)

    def visit_continue_stmt(self, node: 'ContinueStmt', param: List[List['Symbol']]) -> None:
        if self.number_loop == 0: raise MustInLoop(node)

    def visit_if_stmt(self, node: 'IfStmt', param: List[List['Symbol']]) -> None:
        list_condition = [node.condition] + [item[0] for item in node.elif_branches]
        for condition in list_condition:
            type_condition = self.visit(condition, param)
            if not isinstance(type_condition, BoolType):
                raise TypeMismatchInStatement(node)
            
        self.visit(node.then_stmt, param)
        [self.visit(item[1], param) for item in node.elif_branches]
        if node.else_stmt:
            self.visit(node.else_stmt, param)

    def visit_expr_stmt(self, node: 'ExprStmt', param: List[List['Symbol']]) -> None:
        if isinstance(node.expr, FunctionCall):
            if self.curr_function and node.expr.function.name == self.curr_function.name:
                raise Undeclared(FunctionMarker(), node.expr.function.name)
            res: Optional['Symbol'] = next(
                filter(None, map(lambda item_list: self.lookup(node.expr.function.name, item_list, lambda x: x.name), param)),
                None
            )
            if res and isinstance(res.typ, FunctionType):
                type_params = res.typ.param_types
                type_args = [self.visit(item, param) for item in node.expr.args]
                if len(type_params) != len(type_args):
                    raise TypeMismatchInStatement(node)
                if node.expr.function.name == "str":
                    if not isinstance(type_args[0], (IntType, FloatType, BoolType)):
                        raise TypeMismatchInStatement(node)
                else:
                    for param_type, arg_type in zip(type_params, type_args):
                        if not self.compare_types(param_type, arg_type):
                            raise TypeMismatchInStatement(node)
                if not isinstance(res.typ.return_type, VoidType):
                    raise TypeMismatchInStatement(node)
                return
            raise Undeclared(FunctionMarker(), node.expr.function.name)

        elif isinstance(node.expr, BinaryOp) and node.expr.operator == '>>':
            try:
                expr_type = self.visit(node.expr, param)
                if not isinstance(expr_type, VoidType):
                    raise TypeMismatchInStatement(node)
            except TypeMismatchInExpression:
                raise TypeMismatchInStatement(node)

        else:
            self.visit(node.expr, param)

    def visit_id_lvalue(self, node: 'IdLValue', param: List[List['Symbol']]) -> Type:
        for scope in param:
            symbol = self.lookup(node.name, scope, lambda x: x.name)
            if symbol:
                return symbol.typ
        raise Undeclared(IdentifierMarker(), node.name)
    
    def visit_identifier(self, node: 'Identifier', param: List[List['Symbol']]) -> Type:
        for scope in param:
            symbol = self.lookup(node.name, scope, lambda x: x.name)
            if symbol:
                if isinstance(symbol.typ, FunctionType):
                    raise Undeclared(IdentifierMarker(), node.name)
                return symbol.typ
        raise Undeclared(IdentifierMarker(), node.name)
    
    def visit_array_access(self, node: 'ArrayAccess', param: List[List['Symbol']]) -> Type:
        array_type = self.visit(node.array, param)
        index_type = self.visit(node.index, param)
        
        if not isinstance(array_type, ArrayType):
            raise TypeMismatchInExpression(node)
        if not isinstance(index_type, IntType):
            raise TypeMismatchInExpression(node)
        
        return array_type.element_type

    def visit_array_access_lvalue(self, node: 'ArrayAccessLValue', param: List[List['Symbol']]) -> Type:
        array_type = self.visit(node.array, param)
        index_type = self.visit(node.index, param)
        
        if not isinstance(array_type, ArrayType):
            raise TypeMismatchInExpression(node)
        if not isinstance(index_type, IntType):
            raise TypeMismatchInExpression(node)
        
        return array_type.element_type

    def visit_array_literal(self, node: 'ArrayLiteral', param: List[List['Symbol']]) -> Type:
        if not node.elements:
            return ArrayType(IntType(), 0)

        element_types = [self.visit(ele, param) for ele in node.elements]
        first_type = element_types[0]

        for typ in element_types[1:]:
            if not self.compare_types(first_type, typ):
                raise TypeMismatchInExpression(node)

        return ArrayType(first_type, len(element_types))
    
    def visit_array_type(self, node, param): pass

    def visit_binary_op(self, node, param): 
        left_type = self.visit(node.left, param)

        if node.operator == '>>':
            if isinstance(node.right, Identifier):
                res: Optional['Symbol'] = next(
                    filter(None, map(lambda item_list: self.lookup(node.right.name, item_list, lambda x: x.name), param)),
                    None
                )
                if res and isinstance(res.typ, FunctionType):
                    type_params = res.typ.param_types
                    if len(type_params) != 1:
                        raise TypeMismatchInExpression(node)
                    if node.right.name == "str":
                        if not isinstance(left_type, (IntType, FloatType, BoolType)):
                            raise TypeMismatchInExpression(node)
                    else:
                        if not self.compare_types(type_params[0], left_type):
                            raise TypeMismatchInExpression(node)
                    return res.typ.return_type
                raise Undeclared(FunctionMarker(), node.right.name)

            elif isinstance(node.right, FunctionCall):
                res: Optional['Symbol'] = next(
                    filter(None, map(lambda item_list: self.lookup(node.right.function.name, item_list, lambda x: x.name), param)),
                    None
                )
                if res and isinstance(res.typ, FunctionType):
                    type_params = res.typ.param_types
                    type_args = [left_type] + [self.visit(arg, param) for arg in node.right.args]
                    if len(type_params) != len(type_args):
                        raise TypeMismatchInExpression(node)
                    for param_type, arg_type in zip(type_params, type_args):
                        if not self.compare_types(param_type, arg_type):
                            raise TypeMismatchInExpression(node)
                    return res.typ.return_type
                raise Undeclared(FunctionMarker(), node.right.function.name)

            raise TypeMismatchInExpression(node)

        right_type = self.visit(node.right, param)

        if node.operator == '+':
            if (isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType))):
                return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()
            if isinstance(left_type, StringType) and isinstance(right_type, StringType):
                return StringType()
            raise TypeMismatchInExpression(node)

        if node.operator in ['-', '*', '/']:
            if not (isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType))):
                raise TypeMismatchInExpression(node)
            return FloatType() if isinstance(left_type, FloatType) or isinstance(right_type, FloatType) else IntType()

        if node.operator == '%':
            if not (isinstance(left_type, IntType) and isinstance(right_type, IntType)):
                raise TypeMismatchInExpression(node)
            return IntType()

        if node.operator in ['>', '<', '>=', '<=', '==', '!=']:
            if not (isinstance(left_type, (IntType, FloatType, StringType, BoolType)) and 
                    isinstance(right_type, (IntType, FloatType, StringType, BoolType))):
                raise TypeMismatchInExpression(node)
            if node.operator in ['>', '<', '>=', '<=']:
                if not (isinstance(left_type, (IntType, FloatType, StringType)) and 
                        isinstance(right_type, (IntType, FloatType, StringType))):
                    raise TypeMismatchInExpression(node)
            if isinstance(left_type, (IntType, FloatType)) and isinstance(right_type, (IntType, FloatType)):
                return BoolType()
            if not self.compare_types(left_type, right_type):
                raise TypeMismatchInExpression(node)
            return BoolType()

        if node.operator in ['&&', '||']:
            if not self.compare_types(left_type, right_type):
                raise TypeMismatchInExpression(node)
            if not isinstance(left_type, BoolType):
                raise TypeMismatchInExpression(node)
            return BoolType()

        raise TypeMismatchInExpression(node)

    def visit_function_call(self, node: 'FunctionCall', param: List[List['Symbol']]) -> Type:
        if self.curr_function and node.function.name == self.curr_function.name:
            raise Undeclared(FunctionMarker(), node.function.name)

        res: Optional['Symbol'] = next(
            filter(None, map(lambda item_list: self.lookup(node.function.name, item_list, lambda x: x.name), param)),
            None
        )
        if res and isinstance(res.typ, FunctionType):
            type_params = res.typ.param_types
            type_args = [self.visit(item, param) for item in node.args]

            if len(type_params) != len(type_args):
                raise TypeMismatchInExpression(node)

            if node.function.name == "str":  # special case
                if not isinstance(type_args[0], (IntType, FloatType, BoolType)):
                    raise TypeMismatchInExpression(node)
            else:
                for param_type, arg_type in zip(type_params, type_args):
                    if not self.compare_types(param_type, arg_type):
                        raise TypeMismatchInExpression(node)

            if isinstance(res.typ.return_type, VoidType):
                raise TypeMismatchInExpression(node)

            return res.typ.return_type

        raise Undeclared(FunctionMarker(), node.function.name)

    def visit_return_stmt(self, node: 'ReturnStmt', param: List[List['Symbol']]) -> None:
        expected_type = self.curr_function.return_type if self.curr_function else VoidType()

        if node.value is None:
            if not isinstance(expected_type, VoidType):
                raise TypeMismatchInStatement(node)
        else:
            actual_type = self.visit(node.value, param)
            if not self.compare_types(expected_type, actual_type):
                raise TypeMismatchInStatement(node)
        
    def visit_unary_op(self, node: 'UnaryOp', param: List[List['Symbol']]) -> Type:
        operand_type = self.visit(node.operand, param)
        
        if node.operator in ['-', '+']:
            if not isinstance(operand_type, (IntType, FloatType)):
                raise TypeMismatchInExpression(node)
            return operand_type
        
        if node.operator == '!':
            if not isinstance(operand_type, BoolType):
                raise TypeMismatchInExpression(node)
            return BoolType()
        
        raise TypeMismatchInExpression(node)

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