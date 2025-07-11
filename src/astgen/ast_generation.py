"""
AST Generation module for HLang programming language.
This module contains the ASTGeneration class that converts parse trees
into Abstract Syntax Trees using the visitor pattern.
"""

from functools import reduce
from build.HLangVisitor import HLangVisitor
from build.HLangParser import HLangParser
from src.utils.nodes import *

# Visit a parse tree produced by HLangParser.
class ASTGeneration(HLangVisitor):
    # program: constdecl* funcdecl* EOF;
    def visitProgram(self, ctx: HLangParser.ProgramContext):
        consts = [self.visit(decl) for decl in ctx.constdecl()]
        funcs = [self.visit(decl) for decl in ctx.funcdecl()]
        return Program(consts, funcs)

    # constdecl: CONST ID (COLON var_type)? ASSIGN expr SEMICOLON;
    def visitConstdecl(self, ctx: HLangParser.ConstdeclContext):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        typ = self.visit(ctx.var_type()) if ctx.var_type() else None
        return ConstDecl(name, typ, value)

    # vardecl: LET ID (COLON var_type)? ASSIGN expr SEMICOLON;
    def visitVardecl(self, ctx: HLangParser.VardeclContext):
        name = ctx.ID().getText()
        typ = self.visit(ctx.var_type()) if ctx.var_type() else None
        value = self.visit(ctx.expr())
        return VarDecl(name, typ, value)

    # funcdecl: FUNC ID paramdecl ARROW ret_type body;
    def visitFuncdecl(self, ctx: HLangParser.FuncdeclContext):
        name = ctx.ID().getText()
        params = self.visit(ctx.paramdecl())
        rettype = self.visit(ctx.ret_type())
        body = self.visit(ctx.body())
        return FuncDecl(name, params, rettype, body.statements)

    # paramdecl: LP paramlist? RP;
    def visitParamdecl(self, ctx: HLangParser.ParamdeclContext):
        if ctx.paramlist():
            return self.visit(ctx.paramlist())
        return []

    # paramlist: param paramlist_tail;
    def visitParamlist(self, ctx: HLangParser.ParamlistContext):
        param = [self.visit(ctx.param())]
        tail = self.visit(ctx.paramlist_tail())
        return param + tail

    # paramlist_tail: COMMA param paramlist_tail | ;
    def visitParamlist_tail(self, ctx: HLangParser.Paramlist_tailContext):
        if ctx.getChildCount() == 0:
            return []
        param = self.visit(ctx.param())
        tail = self.visit(ctx.paramlist_tail())
        return [param] + tail

    # param: ID COLON var_type;
    def visitParam(self, ctx: HLangParser.ParamContext):
        name = ctx.ID().getText()
        typ = self.visit(ctx.var_type())
        return Param(name, typ)

    # var_type: non_void_type;
    def visitVar_type(self, ctx: HLangParser.Var_typeContext):
        return self.visit(ctx.non_void_type())

    # ret_type: non_void_type | VOID;
    def visitRet_type(self, ctx: HLangParser.Ret_typeContext):
        if ctx.VOID():
            return VoidType()
        return self.visit(ctx.non_void_type())

    # non_void_type: INT | FLOAT | BOOL | STRING | array_type;
    def visitNon_void_type(self, ctx: HLangParser.Non_void_typeContext):
        if ctx.INT():
            return IntType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.BOOL():
            return BoolType()
        if ctx.STRING():
            return StringType()
        return self.visit(ctx.array_type())

    # array_type: LSP non_void_type SEMICOLON INT_LIT RSP;
    def visitArray_type(self, ctx: HLangParser.Array_typeContext):
        ele_type = self.visit(ctx.non_void_type())
        size = int(ctx.INT_LIT().getText())
        return ArrayType(ele_type, size)

    # body: LCP stmt* RCP;
    def visitBody(self, ctx: HLangParser.BodyContext):
        stmts = []
        for stmt in ctx.stmt():
            visited = self.visit(stmt)
            if visited is not None:
                stmts.append(visited)
        return BlockStmt(stmts)
    
    # stmt
    #     : vardecl
    #     | assignment
    #     | callstmt
    #     | returnstmt
    #     | breakstmt
    #     | continuestmt
    #     | if_stmt
    #     | while_stmt
    #     | for_stmt
    #     | exprstmt
    #     | blockstmt
    #     ;
    def visitStmt(self, ctx: HLangParser.StmtContext):
        if ctx.vardecl():
            return self.visit(ctx.vardecl())
        if ctx.assignment():
            return self.visit(ctx.assignment())
        if ctx.callstmt():
            return self.visit(ctx.callstmt())
        if ctx.returnstmt():
            return self.visit(ctx.returnstmt())
        if ctx.breakstmt():
            return self.visit(ctx.breakstmt())
        if ctx.continuestmt():
            return self.visit(ctx.continuestmt())
        if ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        if ctx.while_stmt():
            return self.visit(ctx.while_stmt())
        if ctx.for_stmt():
            return self.visit(ctx.for_stmt())
        if ctx.exprstmt():
            return self.visit(ctx.exprstmt())
        if ctx.blockstmt():
            return self.visit(ctx.blockstmt())
        return None
    
    # assignment: lhs ASSIGN expr SEMICOLON;
    def visitAssignment(self, ctx: HLangParser.AssignmentContext):
        lhs = self.visit(ctx.lhs())  # xử lý phần bên trái
        rhs = self.visit(ctx.expr())  # xử lý phần bên phải
        return Assignment(lhs, rhs)
    
    # lhs: ID lhs_tail;
    def visitLhs(self, ctx: HLangParser.LhsContext):
        name = ctx.ID().getText()
        indices = self.visit(ctx.lhs_tail())
        if not indices:
            return IdLValue(name)
        base = Identifier(name)
        for index in indices[:-1]:
            base = ArrayAccess(base, index)
        return ArrayAccessLValue(base, indices[-1])
    
    # lhs_tail: LSP expr RSP lhs_tail | ;
    def visitLhs_tail(self, ctx: HLangParser.Lhs_tailContext):
        if ctx.getChildCount() == 0:
            return []
        index = self.visit(ctx.expr())
        tail = self.visit(ctx.lhs_tail())
        return [index] + tail
    
    # if_stmt: IF LP expr RP body (ELSE else_stmt)?;
    def visitIf_stmt(self, ctx: HLangParser.If_stmtContext):
        cond = self.visit(ctx.expr())
        thenStmt = self.visit(ctx.body())
        elseStmt = self.visit(ctx.else_stmt()) if ctx.else_stmt() else None
        if isinstance(elseStmt, IfStmt):
            elifs = [(elseStmt.condition, elseStmt.then_stmt)] + elseStmt.elif_branches
            return IfStmt(cond, thenStmt, elifs, elseStmt.else_stmt)
        return IfStmt(cond, thenStmt, [], elseStmt)

    # else_stmt: if_stmt | body;
    def visitElse_stmt(self, ctx: HLangParser.Else_stmtContext):
        if ctx.if_stmt():
            return self.visit(ctx.if_stmt())
        return self.visit(ctx.body())
    
    # while_stmt: WHILE LP expr RP body;
    def visitWhile_stmt(self, ctx: HLangParser.While_stmtContext):
        cond = self.visit(ctx.expr())
        body = self.visit(ctx.body())
        return WhileStmt(cond, body)
    
    # for_stmt: FOR LP ID IN expr RP body;
    def visitFor_stmt(self, ctx: HLangParser.For_stmtContext):
        name = ctx.ID().getText()
        iterable = self.visit(ctx.expr())
        body = self.visit(ctx.body())  # ← phải lấy block đúng
        return ForStmt(name, iterable, body)

    # callstmt: callexpr SEMICOLON;
    def visitCallstmt(self, ctx: HLangParser.CallstmtContext):
        return ExprStmt(self.visit(ctx.callexpr()))
    
    # returnstmt: RETURN expr? SEMICOLON;
    def visitReturnstmt(self, ctx: HLangParser.ReturnstmtContext):
        if ctx.expr():
            return ReturnStmt(self.visit(ctx.expr()))
        return ReturnStmt(None)
    
    # exprstmt: expr SEMICOLON;
    def visitExprstmt(self, ctx: HLangParser.ExprstmtContext):
        return ExprStmt(self.visit(ctx.expr()))
    
    # breakstmt: BREAK SEMICOLON;
    def visitBreakstmt(self, ctx: HLangParser.BreakstmtContext):
        return BreakStmt()

    # continuestmt: CONTINUE SEMICOLON;
    def visitContinuestmt(self, ctx: HLangParser.ContinuestmtContext):
        return ContinueStmt()
    
    # blockstmt: LCP stmt* RCP;
    def visitBlockstmt(self, ctx: HLangParser.BlockstmtContext):
        stmts = []
        for stmt_ctx in ctx.stmt():
            stmt = self.visit(stmt_ctx)
            if stmt is not None:
                stmts.append(stmt)
        return BlockStmt(stmts)

    # expr: expr1;
    def visitExpr(self, ctx: HLangParser.ExprContext):
        return self.visit(ctx.expr1())

    # expr1: expr2;
    def visitExpr1(self, ctx: HLangParser.Expr1Context):
        return self.visit(ctx.expr2())

    # expr2: expr2 PIPELINE expr3 | expr3;
    def visitExpr2(self, ctx: HLangParser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr3())

        operands = []
        current = ctx
        while isinstance(current, HLangParser.Expr2Context) and current.PIPELINE():
            operands.append(self.visit(current.expr3()))
            current = current.expr2()
        operands.append(self.visit(current.expr3()))
        operands = list(reversed(operands))

        result = operands[0]
        for op in operands[1:]:
            result = BinaryOp(result, ">>", op)
        return result

    # expr3: expr3 OR expr4 | expr4;
    def visitExpr3(self, ctx: HLangParser.Expr3Context):
        if ctx.OR():
            left = self.visit(ctx.expr3())
            right = self.visit(ctx.expr4())
            return BinaryOp(left, "||", right)
        return self.visit(ctx.expr4())

    # expr4: expr4 AND expr5 | expr5;
    def visitExpr4(self, ctx: HLangParser.Expr4Context):
        if ctx.AND():
            left = self.visit(ctx.expr4())
            right = self.visit(ctx.expr5())
            return BinaryOp(left, "&&", right)
        return self.visit(ctx.expr5())

    # expr5: expr5 (EQUAL | UNEQUAL) expr6 | expr6;
    def visitExpr5(self, ctx: HLangParser.Expr5Context):
        if ctx.EQUAL():
            left = self.visit(ctx.expr5())
            right = self.visit(ctx.expr6())
            return BinaryOp(left, "==", right)
        elif ctx.UNEQUAL():
            left = self.visit(ctx.expr5())
            right = self.visit(ctx.expr6())
            return BinaryOp(left, "!=", right)
        return self.visit(ctx.expr6())

    # expr6: expr6 (LT | LTE | GT | GTE) expr7 | expr7;
    def visitExpr6(self, ctx: HLangParser.Expr6Context):
        if ctx.LT():
            left = self.visit(ctx.expr6())
            right = self.visit(ctx.expr7())
            return BinaryOp(left, "<", right)
        elif ctx.LTE():
            left = self.visit(ctx.expr6())
            right = self.visit(ctx.expr7())
            return BinaryOp(left, "<=", right)
        elif ctx.GT():
            left = self.visit(ctx.expr6())
            right = self.visit(ctx.expr7())
            return BinaryOp(left, ">", right)
        elif ctx.GTE():
            left = self.visit(ctx.expr6())
            right = self.visit(ctx.expr7())
            return BinaryOp(left, ">=", right)
        return self.visit(ctx.expr7())

    # expr7: expr7 (ADD | SUB) expr8 | expr8;
    def visitExpr7(self, ctx: HLangParser.Expr7Context):
        if ctx.ADD():
            left = self.visit(ctx.expr7())
            right = self.visit(ctx.expr8())
            return BinaryOp(left, "+", right)
        elif ctx.SUB():
            left = self.visit(ctx.expr7())
            right = self.visit(ctx.expr8())
            return BinaryOp(left, "-", right)
        return self.visit(ctx.expr8())

    # expr8: expr8 (MUL | DIV | MOD) expr9 | expr9;
    def visitExpr8(self, ctx: HLangParser.Expr8Context):
        if ctx.MUL():
            left = self.visit(ctx.expr8())
            right = self.visit(ctx.expr9())
            return BinaryOp(left, "*", right)
        elif ctx.DIV():
            left = self.visit(ctx.expr8())
            right = self.visit(ctx.expr9())
            return BinaryOp(left, "/", right)
        elif ctx.MOD():
            left = self.visit(ctx.expr8())
            right = self.visit(ctx.expr9())
            return BinaryOp(left, "%", right)
        return self.visit(ctx.expr9())

    # expr9: (NOT | SUB | ADD) expr9 | primary_expr expr9_tail;
    def visitExpr9(self, ctx: HLangParser.Expr9Context):
        if ctx.NOT():
            return UnaryOp("!", self.visit(ctx.expr9()))
        elif ctx.SUB():
            return UnaryOp("-", self.visit(ctx.expr9()))
        elif ctx.ADD():
            return UnaryOp("+", self.visit(ctx.expr9()))

        base = self.visit(ctx.primary_expr())

        if isinstance(base, IdLValue):
            base = Identifier(base.name)

        indices = self.visit(ctx.expr9_tail())
        if not indices:
            return base

        return reduce(lambda acc, idx: ArrayAccess(acc, idx), indices, base)

    # expr9_tail: LSP expr RSP expr9_tail | ;
    def visitExpr9_tail(self, ctx: HLangParser.Expr9_tailContext):
        if ctx.getChildCount() == 0:
            return []
        index = self.visit(ctx.expr())
        tail = self.visit(ctx.expr9_tail())
        return [index] + tail

    # primary_expr:
    #     INT_LIT
    #     | FLOAT_LIT
    #     | STRING_LIT
    #     | TRUE
    #     | FALSE
    #     | array_lit
    #     | type_conversion_call
    #     | callexpr
    #     | ID
    #     | LP expr RP
    def visitPrimary_expr(self, ctx: HLangParser.Primary_exprContext):
        if ctx.INT_LIT():
            return IntegerLiteral(int(ctx.INT_LIT().getText()))
        elif ctx.FLOAT_LIT():
            return FloatLiteral(float(ctx.FLOAT_LIT().getText()))
        elif ctx.STRING_LIT():
            return StringLiteral(ctx.STRING_LIT().getText())
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.array_lit():
            return self.visit(ctx.array_lit())
        elif ctx.callexpr():
            return self.visit(ctx.callexpr())
        elif ctx.type_conversion_call():
            return self.visit(ctx.type_conversion_call())
        elif ctx.ID():
            return Identifier(ctx.ID().getText())
        elif ctx.expr():
            return self.visit(ctx.expr())  # Trường hợp (expr)
        return None
    
    # type_conversion_call
    #     : INT LP exprlist_opt RP
    #     | FLOAT LP exprlist_opt RP
    #     | STR LP exprlist_opt RP
    #     ;
    def visitType_conversion_call(self, ctx: HLangParser.Type_conversion_callContext):
        func_name = ""
        if ctx.INT():
            func_name = "int"
        elif ctx.FLOAT():
            func_name = "float"
        elif ctx.STR():
            func_name = "str"
        
        args = self.visit(ctx.exprlist_opt())
        return FunctionCall(Identifier(func_name), args)
    
    # callexpr: ID LP exprlist_opt RP ;
    def visitCallexpr(self, ctx: HLangParser.CallexprContext):
        name = ctx.ID().getText()
        args = self.visit(ctx.exprlist_opt())
        return FunctionCall(Identifier(name), args)
    
    # array_lit: LSP exprlist_opt RSP ;
    def visitArray_lit(self, ctx: HLangParser.Array_litContext):
        return ArrayLiteral(self.visit(ctx.exprlist_opt()))
    
    # exprlist_opt: exprlist | ;
    def visitExprlist_opt(self, ctx: HLangParser.Exprlist_optContext):
        if ctx.getChildCount() == 0:
            return []  # empty list: ()
        return self.visit(ctx.exprlist())

    # exprlist: expr exprlist_tail ;
    def visitExprlist(self, ctx: HLangParser.ExprlistContext):
        return [self.visit(ctx.expr())] + self.visit(ctx.exprlist_tail())
    
    # exprlist_tail: COMMA expr exprlist_tail | ;
    def visitExprlist_tail(self, ctx: HLangParser.Exprlist_tailContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.expr())] + self.visit(ctx.exprlist_tail())