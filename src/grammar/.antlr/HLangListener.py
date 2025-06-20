# Generated from c://Users//PC//hlang-compiler//src//grammar//HLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .HLangParser import HLangParser
else:
    from HLangParser import HLangParser

# This class defines a complete listener for a parse tree produced by HLangParser.
class HLangListener(ParseTreeListener):

    # Enter a parse tree produced by HLangParser#program.
    def enterProgram(self, ctx:HLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by HLangParser#program.
    def exitProgram(self, ctx:HLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by HLangParser#decl.
    def enterDecl(self, ctx:HLangParser.DeclContext):
        pass

    # Exit a parse tree produced by HLangParser#decl.
    def exitDecl(self, ctx:HLangParser.DeclContext):
        pass


    # Enter a parse tree produced by HLangParser#vardecl.
    def enterVardecl(self, ctx:HLangParser.VardeclContext):
        pass

    # Exit a parse tree produced by HLangParser#vardecl.
    def exitVardecl(self, ctx:HLangParser.VardeclContext):
        pass


    # Enter a parse tree produced by HLangParser#funcdecl.
    def enterFuncdecl(self, ctx:HLangParser.FuncdeclContext):
        pass

    # Exit a parse tree produced by HLangParser#funcdecl.
    def exitFuncdecl(self, ctx:HLangParser.FuncdeclContext):
        pass


    # Enter a parse tree produced by HLangParser#block.
    def enterBlock(self, ctx:HLangParser.BlockContext):
        pass

    # Exit a parse tree produced by HLangParser#block.
    def exitBlock(self, ctx:HLangParser.BlockContext):
        pass


    # Enter a parse tree produced by HLangParser#stmt.
    def enterStmt(self, ctx:HLangParser.StmtContext):
        pass

    # Exit a parse tree produced by HLangParser#stmt.
    def exitStmt(self, ctx:HLangParser.StmtContext):
        pass


    # Enter a parse tree produced by HLangParser#funcall.
    def enterFuncall(self, ctx:HLangParser.FuncallContext):
        pass

    # Exit a parse tree produced by HLangParser#funcall.
    def exitFuncall(self, ctx:HLangParser.FuncallContext):
        pass


    # Enter a parse tree produced by HLangParser#exp.
    def enterExp(self, ctx:HLangParser.ExpContext):
        pass

    # Exit a parse tree produced by HLangParser#exp.
    def exitExp(self, ctx:HLangParser.ExpContext):
        pass



del HLangParser