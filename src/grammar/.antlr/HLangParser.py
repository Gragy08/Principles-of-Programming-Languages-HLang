# Generated from c://Users//PC//hlang-compiler//src//grammar//HLang.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,56,366,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,1,0,5,0,80,
        8,0,10,0,12,0,83,9,0,1,0,1,0,1,1,1,1,3,1,89,8,1,1,2,1,2,1,2,1,2,
        3,2,95,8,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,105,8,3,1,3,1,3,1,
        3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,6,1,6,3,6,122,8,6,1,
        7,1,7,1,7,1,7,1,7,3,7,129,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,
        9,5,9,140,8,9,10,9,12,9,143,9,9,1,10,1,10,3,10,147,8,10,1,10,1,10,
        1,11,1,11,1,11,5,11,154,8,11,10,11,12,11,157,9,11,1,12,1,12,1,12,
        1,12,1,13,1,13,5,13,165,8,13,10,13,12,13,168,9,13,1,13,1,13,1,14,
        1,14,1,14,1,14,1,14,1,14,1,14,1,14,3,14,180,8,14,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,3,17,203,8,17,1,18,1,18,1,18,1,18,1,18,
        1,19,1,19,1,19,1,19,1,19,5,19,215,8,19,10,19,12,19,218,9,19,1,20,
        1,20,1,20,1,21,1,21,3,21,225,8,21,1,21,1,21,1,22,1,22,1,22,1,23,
        1,23,1,24,1,24,1,24,1,24,1,24,1,24,5,24,240,8,24,10,24,12,24,243,
        9,24,1,25,1,25,1,25,1,25,1,25,1,25,5,25,251,8,25,10,25,12,25,254,
        9,25,1,26,1,26,1,26,1,26,1,26,1,26,5,26,262,8,26,10,26,12,26,265,
        9,26,1,27,1,27,1,27,1,27,1,27,1,27,5,27,273,8,27,10,27,12,27,276,
        9,27,1,28,1,28,1,28,1,28,1,28,1,28,5,28,284,8,28,10,28,12,28,287,
        9,28,1,29,1,29,1,29,1,29,1,29,1,29,5,29,295,8,29,10,29,12,29,298,
        9,29,1,30,1,30,1,30,1,30,1,30,1,30,5,30,306,8,30,10,30,12,30,309,
        9,30,1,31,1,31,1,31,3,31,314,8,31,1,32,1,32,1,32,1,32,1,32,5,32,
        321,8,32,10,32,12,32,324,9,32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,
        1,33,1,33,1,33,1,33,1,33,3,33,338,8,33,1,34,1,34,1,34,1,34,1,34,
        1,35,1,35,3,35,347,8,35,1,36,1,36,1,37,1,37,1,37,1,37,1,38,1,38,
        1,38,5,38,358,8,38,10,38,12,38,361,9,38,1,38,3,38,364,8,38,1,38,
        0,7,48,50,52,54,56,58,60,39,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,
        72,74,76,0,6,1,0,24,25,1,0,26,29,1,0,19,20,1,0,21,23,2,0,19,20,32,
        32,3,0,7,7,12,12,15,15,369,0,81,1,0,0,0,2,88,1,0,0,0,4,90,1,0,0,
        0,6,100,1,0,0,0,8,110,1,0,0,0,10,117,1,0,0,0,12,121,1,0,0,0,14,128,
        1,0,0,0,16,130,1,0,0,0,18,136,1,0,0,0,20,144,1,0,0,0,22,150,1,0,
        0,0,24,158,1,0,0,0,26,162,1,0,0,0,28,179,1,0,0,0,30,181,1,0,0,0,
        32,189,1,0,0,0,34,195,1,0,0,0,36,204,1,0,0,0,38,209,1,0,0,0,40,219,
        1,0,0,0,42,222,1,0,0,0,44,228,1,0,0,0,46,231,1,0,0,0,48,233,1,0,
        0,0,50,244,1,0,0,0,52,255,1,0,0,0,54,266,1,0,0,0,56,277,1,0,0,0,
        58,288,1,0,0,0,60,299,1,0,0,0,62,313,1,0,0,0,64,315,1,0,0,0,66,337,
        1,0,0,0,68,339,1,0,0,0,70,346,1,0,0,0,72,348,1,0,0,0,74,350,1,0,
        0,0,76,363,1,0,0,0,78,80,3,2,1,0,79,78,1,0,0,0,80,83,1,0,0,0,81,
        79,1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,0,83,81,1,0,0,0,84,85,5,0,0,
        1,85,1,1,0,0,0,86,89,3,4,2,0,87,89,3,8,4,0,88,86,1,0,0,0,88,87,1,
        0,0,0,89,3,1,0,0,0,90,91,5,3,0,0,91,94,5,46,0,0,92,93,5,34,0,0,93,
        95,3,10,5,0,94,92,1,0,0,0,94,95,1,0,0,0,95,96,1,0,0,0,96,97,5,33,
        0,0,97,98,3,46,23,0,98,99,5,44,0,0,99,5,1,0,0,0,100,101,5,13,0,0,
        101,104,5,46,0,0,102,103,5,34,0,0,103,105,3,10,5,0,104,102,1,0,0,
        0,104,105,1,0,0,0,105,106,1,0,0,0,106,107,5,33,0,0,107,108,3,46,
        23,0,108,109,5,44,0,0,109,7,1,0,0,0,110,111,5,9,0,0,111,112,5,46,
        0,0,112,113,3,20,10,0,113,114,5,35,0,0,114,115,3,12,6,0,115,116,
        3,26,13,0,116,9,1,0,0,0,117,118,3,14,7,0,118,11,1,0,0,0,119,122,
        3,14,7,0,120,122,5,17,0,0,121,119,1,0,0,0,121,120,1,0,0,0,122,13,
        1,0,0,0,123,129,5,12,0,0,124,129,5,7,0,0,125,129,5,1,0,0,126,129,
        5,15,0,0,127,129,3,16,8,0,128,123,1,0,0,0,128,124,1,0,0,0,128,125,
        1,0,0,0,128,126,1,0,0,0,128,127,1,0,0,0,129,15,1,0,0,0,130,131,5,
        41,0,0,131,132,3,14,7,0,132,133,5,44,0,0,133,134,5,47,0,0,134,135,
        5,42,0,0,135,17,1,0,0,0,136,141,5,46,0,0,137,138,5,43,0,0,138,140,
        5,46,0,0,139,137,1,0,0,0,140,143,1,0,0,0,141,139,1,0,0,0,141,142,
        1,0,0,0,142,19,1,0,0,0,143,141,1,0,0,0,144,146,5,37,0,0,145,147,
        3,22,11,0,146,145,1,0,0,0,146,147,1,0,0,0,147,148,1,0,0,0,148,149,
        5,38,0,0,149,21,1,0,0,0,150,155,3,24,12,0,151,152,5,43,0,0,152,154,
        3,24,12,0,153,151,1,0,0,0,154,157,1,0,0,0,155,153,1,0,0,0,155,156,
        1,0,0,0,156,23,1,0,0,0,157,155,1,0,0,0,158,159,5,46,0,0,159,160,
        5,34,0,0,160,161,3,10,5,0,161,25,1,0,0,0,162,166,5,39,0,0,163,165,
        3,28,14,0,164,163,1,0,0,0,165,168,1,0,0,0,166,164,1,0,0,0,166,167,
        1,0,0,0,167,169,1,0,0,0,168,166,1,0,0,0,169,170,5,40,0,0,170,27,
        1,0,0,0,171,180,3,6,3,0,172,180,3,36,18,0,173,180,3,40,20,0,174,
        180,3,42,21,0,175,180,3,34,17,0,176,180,3,32,16,0,177,180,3,30,15,
        0,178,180,3,44,22,0,179,171,1,0,0,0,179,172,1,0,0,0,179,173,1,0,
        0,0,179,174,1,0,0,0,179,175,1,0,0,0,179,176,1,0,0,0,179,177,1,0,
        0,0,179,178,1,0,0,0,180,29,1,0,0,0,181,182,5,8,0,0,182,183,5,37,
        0,0,183,184,5,46,0,0,184,185,5,11,0,0,185,186,3,46,23,0,186,187,
        5,38,0,0,187,188,3,26,13,0,188,31,1,0,0,0,189,190,5,18,0,0,190,191,
        5,37,0,0,191,192,3,46,23,0,192,193,5,38,0,0,193,194,3,26,13,0,194,
        33,1,0,0,0,195,196,5,10,0,0,196,197,5,37,0,0,197,198,3,46,23,0,198,
        199,5,38,0,0,199,202,3,26,13,0,200,201,5,5,0,0,201,203,3,26,13,0,
        202,200,1,0,0,0,202,203,1,0,0,0,203,35,1,0,0,0,204,205,3,38,19,0,
        205,206,5,33,0,0,206,207,3,46,23,0,207,208,5,44,0,0,208,37,1,0,0,
        0,209,216,5,46,0,0,210,211,5,41,0,0,211,212,3,46,23,0,212,213,5,
        42,0,0,213,215,1,0,0,0,214,210,1,0,0,0,215,218,1,0,0,0,216,214,1,
        0,0,0,216,217,1,0,0,0,217,39,1,0,0,0,218,216,1,0,0,0,219,220,3,68,
        34,0,220,221,5,44,0,0,221,41,1,0,0,0,222,224,5,14,0,0,223,225,3,
        46,23,0,224,223,1,0,0,0,224,225,1,0,0,0,225,226,1,0,0,0,226,227,
        5,44,0,0,227,43,1,0,0,0,228,229,3,46,23,0,229,230,5,44,0,0,230,45,
        1,0,0,0,231,232,3,48,24,0,232,47,1,0,0,0,233,234,6,24,-1,0,234,235,
        3,50,25,0,235,241,1,0,0,0,236,237,10,2,0,0,237,238,5,31,0,0,238,
        240,3,50,25,0,239,236,1,0,0,0,240,243,1,0,0,0,241,239,1,0,0,0,241,
        242,1,0,0,0,242,49,1,0,0,0,243,241,1,0,0,0,244,245,6,25,-1,0,245,
        246,3,52,26,0,246,252,1,0,0,0,247,248,10,2,0,0,248,249,5,30,0,0,
        249,251,3,52,26,0,250,247,1,0,0,0,251,254,1,0,0,0,252,250,1,0,0,
        0,252,253,1,0,0,0,253,51,1,0,0,0,254,252,1,0,0,0,255,256,6,26,-1,
        0,256,257,3,54,27,0,257,263,1,0,0,0,258,259,10,2,0,0,259,260,7,0,
        0,0,260,262,3,54,27,0,261,258,1,0,0,0,262,265,1,0,0,0,263,261,1,
        0,0,0,263,264,1,0,0,0,264,53,1,0,0,0,265,263,1,0,0,0,266,267,6,27,
        -1,0,267,268,3,56,28,0,268,274,1,0,0,0,269,270,10,2,0,0,270,271,
        7,1,0,0,271,273,3,56,28,0,272,269,1,0,0,0,273,276,1,0,0,0,274,272,
        1,0,0,0,274,275,1,0,0,0,275,55,1,0,0,0,276,274,1,0,0,0,277,278,6,
        28,-1,0,278,279,3,58,29,0,279,285,1,0,0,0,280,281,10,2,0,0,281,282,
        7,2,0,0,282,284,3,58,29,0,283,280,1,0,0,0,284,287,1,0,0,0,285,283,
        1,0,0,0,285,286,1,0,0,0,286,57,1,0,0,0,287,285,1,0,0,0,288,289,6,
        29,-1,0,289,290,3,60,30,0,290,296,1,0,0,0,291,292,10,2,0,0,292,293,
        7,3,0,0,293,295,3,60,30,0,294,291,1,0,0,0,295,298,1,0,0,0,296,294,
        1,0,0,0,296,297,1,0,0,0,297,59,1,0,0,0,298,296,1,0,0,0,299,300,6,
        30,-1,0,300,301,3,62,31,0,301,307,1,0,0,0,302,303,10,2,0,0,303,304,
        5,36,0,0,304,306,3,62,31,0,305,302,1,0,0,0,306,309,1,0,0,0,307,305,
        1,0,0,0,307,308,1,0,0,0,308,61,1,0,0,0,309,307,1,0,0,0,310,311,7,
        4,0,0,311,314,3,62,31,0,312,314,3,64,32,0,313,310,1,0,0,0,313,312,
        1,0,0,0,314,63,1,0,0,0,315,322,3,66,33,0,316,317,5,41,0,0,317,318,
        3,46,23,0,318,319,5,42,0,0,319,321,1,0,0,0,320,316,1,0,0,0,321,324,
        1,0,0,0,322,320,1,0,0,0,322,323,1,0,0,0,323,65,1,0,0,0,324,322,1,
        0,0,0,325,338,5,47,0,0,326,338,5,48,0,0,327,338,5,49,0,0,328,338,
        5,16,0,0,329,338,5,6,0,0,330,338,3,74,37,0,331,338,3,68,34,0,332,
        338,5,46,0,0,333,334,5,37,0,0,334,335,3,46,23,0,335,336,5,38,0,0,
        336,338,1,0,0,0,337,325,1,0,0,0,337,326,1,0,0,0,337,327,1,0,0,0,
        337,328,1,0,0,0,337,329,1,0,0,0,337,330,1,0,0,0,337,331,1,0,0,0,
        337,332,1,0,0,0,337,333,1,0,0,0,338,67,1,0,0,0,339,340,3,70,35,0,
        340,341,5,37,0,0,341,342,3,76,38,0,342,343,5,38,0,0,343,69,1,0,0,
        0,344,347,5,46,0,0,345,347,3,72,36,0,346,344,1,0,0,0,346,345,1,0,
        0,0,347,71,1,0,0,0,348,349,7,5,0,0,349,73,1,0,0,0,350,351,5,41,0,
        0,351,352,3,76,38,0,352,353,5,42,0,0,353,75,1,0,0,0,354,359,3,46,
        23,0,355,356,5,43,0,0,356,358,3,46,23,0,357,355,1,0,0,0,358,361,
        1,0,0,0,359,357,1,0,0,0,359,360,1,0,0,0,360,364,1,0,0,0,361,359,
        1,0,0,0,362,364,1,0,0,0,363,354,1,0,0,0,363,362,1,0,0,0,364,77,1,
        0,0,0,27,81,88,94,104,121,128,141,146,155,166,179,202,216,224,241,
        252,263,274,285,296,307,313,322,337,346,359,363
    ]

class HLangParser ( Parser ):

    grammarFileName = "HLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'bool'", "'break'", "'const'", "'continue'", 
                     "'else'", "'false'", "'float'", "'for'", "'func'", 
                     "'if'", "'in'", "'int'", "'let'", "'return'", "'string'", 
                     "'true'", "'void'", "'while'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'=='", "'!='", "'<'", "'<='", "'>'", 
                     "'>='", "'&&'", "'||'", "'!'", "'='", "':'", "'->'", 
                     "'>>'", "'('", "')'", "'{'", "'}'", "'['", "']'", "','", 
                     "';'", "'.'" ]

    symbolicNames = [ "<INVALID>", "BOOL", "BREAK", "CONST", "CONTINUE", 
                      "ELSE", "FALSE", "FLOAT", "FOR", "FUNC", "IF", "IN", 
                      "INT", "LET", "RETURN", "STRING", "TRUE", "VOID", 
                      "WHILE", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", 
                      "UNEQUAL", "LT", "LTE", "GT", "GTE", "AND", "OR", 
                      "NOT", "ASSIGN", "COLON", "ARROW", "PIPELINE", "LP", 
                      "RP", "LCP", "RCP", "LSP", "RSP", "COMMA", "SEMICOLON", 
                      "DOT", "ID", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
                      "WS", "NEWLINE", "COMMENT_LINE", "COMMENT", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_constdecl = 2
    RULE_vardecl = 3
    RULE_funcdecl = 4
    RULE_var_type = 5
    RULE_ret_type = 6
    RULE_non_void_type = 7
    RULE_array_type = 8
    RULE_idlist = 9
    RULE_paramdecl = 10
    RULE_paramlist = 11
    RULE_param = 12
    RULE_body = 13
    RULE_stmt = 14
    RULE_for_stmt = 15
    RULE_while_stmt = 16
    RULE_if_stmt = 17
    RULE_assignment = 18
    RULE_lhs = 19
    RULE_callstmt = 20
    RULE_returnstmt = 21
    RULE_exprstmt = 22
    RULE_expr = 23
    RULE_expr1 = 24
    RULE_expr2 = 25
    RULE_expr3 = 26
    RULE_expr4 = 27
    RULE_expr5 = 28
    RULE_expr6 = 29
    RULE_expr7 = 30
    RULE_expr8 = 31
    RULE_expr9 = 32
    RULE_primary_expr = 33
    RULE_callexpr = 34
    RULE_callee = 35
    RULE_builtin_func = 36
    RULE_array_lit = 37
    RULE_exprlist = 38

    ruleNames =  [ "program", "decl", "constdecl", "vardecl", "funcdecl", 
                   "var_type", "ret_type", "non_void_type", "array_type", 
                   "idlist", "paramdecl", "paramlist", "param", "body", 
                   "stmt", "for_stmt", "while_stmt", "if_stmt", "assignment", 
                   "lhs", "callstmt", "returnstmt", "exprstmt", "expr", 
                   "expr1", "expr2", "expr3", "expr4", "expr5", "expr6", 
                   "expr7", "expr8", "expr9", "primary_expr", "callexpr", 
                   "callee", "builtin_func", "array_lit", "exprlist" ]

    EOF = Token.EOF
    BOOL=1
    BREAK=2
    CONST=3
    CONTINUE=4
    ELSE=5
    FALSE=6
    FLOAT=7
    FOR=8
    FUNC=9
    IF=10
    IN=11
    INT=12
    LET=13
    RETURN=14
    STRING=15
    TRUE=16
    VOID=17
    WHILE=18
    ADD=19
    SUB=20
    MUL=21
    DIV=22
    MOD=23
    EQUAL=24
    UNEQUAL=25
    LT=26
    LTE=27
    GT=28
    GTE=29
    AND=30
    OR=31
    NOT=32
    ASSIGN=33
    COLON=34
    ARROW=35
    PIPELINE=36
    LP=37
    RP=38
    LCP=39
    RCP=40
    LSP=41
    RSP=42
    COMMA=43
    SEMICOLON=44
    DOT=45
    ID=46
    INT_LIT=47
    FLOAT_LIT=48
    STRING_LIT=49
    WS=50
    NEWLINE=51
    COMMENT_LINE=52
    COMMENT=53
    UNCLOSE_STRING=54
    ILLEGAL_ESCAPE=55
    ERROR_CHAR=56

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(HLangParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HLangParser.DeclContext)
            else:
                return self.getTypedRuleContext(HLangParser.DeclContext,i)


        def getRuleIndex(self):
            return HLangParser.RULE_program




    def program(self):

        localctx = HLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==9:
                self.state = 78
                self.decl()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(HLangParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constdecl(self):
            return self.getTypedRuleContext(HLangParser.ConstdeclContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(HLangParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return HLangParser.RULE_decl




    def decl(self):

        localctx = HLangParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 88
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.constdecl()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.funcdecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(HLangParser.CONST, 0)

        def ID(self):
            return self.getToken(HLangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(HLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(HLangParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(HLangParser.SEMICOLON, 0)

        def COLON(self):
            return self.getToken(HLangParser.COLON, 0)

        def var_type(self):
            return self.getTypedRuleContext(HLangParser.Var_typeContext,0)


        def getRuleIndex(self):
            return HLangParser.RULE_constdecl




    def constdecl(self):

        localctx = HLangParser.ConstdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_constdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(HLangParser.CONST)
            self.state = 91
            self.match(HLangParser.ID)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 92
                self.match(HLangParser.COLON)
                self.state = 93
                self.var_type()


            self.state = 96
            self.match(HLangParser.ASSIGN)
            self.state = 97
            self.expr()
            self.state = 98
            self.match(HLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LET(self):
            return self.getToken(HLangParser.LET, 0)

        def ID(self):
            return self.getToken(HLangParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(HLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(HLangParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(HLangParser.SEMICOLON, 0)

        def COLON(self):
            return self.getToken(HLangParser.COLON, 0)

        def var_type(self):
            return self.getTypedRuleContext(HLangParser.Var_typeContext,0)


        def getRuleIndex(self):
            return HLangParser.RULE_vardecl




    def vardecl(self):

        localctx = HLangParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(HLangParser.LET)
            self.state = 101
            self.match(HLangParser.ID)
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 102
                self.match(HLangParser.COLON)
                self.state = 103
                self.var_type()


            self.state = 106
            self.match(HLangParser.ASSIGN)
            self.state = 107
            self.expr()
            self.state = 108
            self.match(HLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(HLangParser.FUNC, 0)

        def ID(self):
            return self.getToken(HLangParser.ID, 0)

        def paramdecl(self):
            return self.getTypedRuleContext(HLangParser.ParamdeclContext,0)


        def ARROW(self):
            return self.getToken(HLangParser.ARROW, 0)

        def ret_type(self):
            return self.getTypedRuleContext(HLangParser.Ret_typeContext,0)


        def body(self):
            return self.getTypedRuleContext(HLangParser.BodyContext,0)


        def getRuleIndex(self):
            return HLangParser.RULE_funcdecl




    def funcdecl(self):

        localctx = HLangParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(HLangParser.FUNC)
            self.state = 111
            self.match(HLangParser.ID)
            self.state = 112
            self.paramdecl()
            self.state = 113
            self.match(HLangParser.ARROW)
            self.state = 114
            self.ret_type()
            self.state = 115
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def non_void_type(self):
            return self.getTypedRuleContext(HLangParser.Non_void_typeContext,0)


        def getRuleIndex(self):
            return HLangParser.RULE_var_type




    def var_type(self):

        localctx = HLangParser.Var_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.non_void_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ret_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def non_void_type(self):
            return self.getTypedRuleContext(HLangParser.Non_void_typeContext,0)


        def VOID(self):
            return self.getToken(HLangParser.VOID, 0)

        def getRuleIndex(self):
            return HLangParser.RULE_ret_type




    def ret_type(self):

        localctx = HLangParser.Ret_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ret_type)
        try:
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 7, 12, 15, 41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 119
                self.non_void_type()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 120
                self.match(HLangParser.VOID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Non_void_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(HLangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(HLangParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(HLangParser.BOOL, 0)

        def STRING(self):
            return self.getToken(HLangParser.STRING, 0)

        def array_type(self):
            return self.getTypedRuleContext(HLangParser.Array_typeContext,0)


        def getRuleIndex(self):
            return HLangParser.RULE_non_void_type




    def non_void_type(self):

        localctx = HLangParser.Non_void_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_non_void_type)
        try:
            self.state = 128
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.match(HLangParser.INT)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.match(HLangParser.FLOAT)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 125
                self.match(HLangParser.BOOL)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 4)
                self.state = 126
                self.match(HLangParser.STRING)
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 5)
                self.state = 127
                self.array_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSP(self):
            return self.getToken(HLangParser.LSP, 0)

        def non_void_type(self):
            return self.getTypedRuleContext(HLangParser.Non_void_typeContext,0)


        def SEMICOLON(self):
            return self.getToken(HLangParser.SEMICOLON, 0)

        def INT_LIT(self):
            return self.getToken(HLangParser.INT_LIT, 0)

        def RSP(self):
            return self.getToken(HLangParser.RSP, 0)

        def getRuleIndex(self):
            return HLangParser.RULE_array_type




    def array_type(self):

        localctx = HLangParser.Array_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(HLangParser.LSP)
            self.state = 131
            self.non_void_type()
            self.state = 132
            self.match(HLangParser.SEMICOLON)
            self.state = 133
            self.match(HLangParser.INT_LIT)
            self.state = 134
            self.match(HLangParser.RSP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.ID)
            else:
                return self.getToken(HLangParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.COMMA)
            else:
                return self.getToken(HLangParser.COMMA, i)

        def getRuleIndex(self):
            return HLangParser.RULE_idlist




    def idlist(self):

        localctx = HLangParser.IdlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_idlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(HLangParser.ID)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 137
                self.match(HLangParser.COMMA)
                self.state = 138
                self.match(HLangParser.ID)
                self.state = 143
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(HLangParser.LP, 0)

        def RP(self):
            return self.getToken(HLangParser.RP, 0)

        def paramlist(self):
            return self.getTypedRuleContext(HLangParser.ParamlistContext,0)


        def getRuleIndex(self):
            return HLangParser.RULE_paramdecl




    def paramdecl(self):

        localctx = HLangParser.ParamdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_paramdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(HLangParser.LP)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 145
                self.paramlist()


            self.state = 148
            self.match(HLangParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HLangParser.ParamContext)
            else:
                return self.getTypedRuleContext(HLangParser.ParamContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.COMMA)
            else:
                return self.getToken(HLangParser.COMMA, i)

        def getRuleIndex(self):
            return HLangParser.RULE_paramlist




    def paramlist(self):

        localctx = HLangParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_paramlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.param()
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==43:
                self.state = 151
                self.match(HLangParser.COMMA)
                self.state = 152
                self.param()
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(HLangParser.ID, 0)

        def COLON(self):
            return self.getToken(HLangParser.COLON, 0)

        def var_type(self):
            return self.getTypedRuleContext(HLangParser.Var_typeContext,0)


        def getRuleIndex(self):
            return HLangParser.RULE_param




    def param(self):

        localctx = HLangParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(HLangParser.ID)
            self.state = 159
            self.match(HLangParser.COLON)
            self.state = 160
            self.var_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCP(self):
            return self.getToken(HLangParser.LCP, 0)

        def RCP(self):
            return self.getToken(HLangParser.RCP, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HLangParser.StmtContext)
            else:
                return self.getTypedRuleContext(HLangParser.StmtContext,i)


        def getRuleIndex(self):
            return HLangParser.RULE_body




    def body(self):

        localctx = HLangParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(HLangParser.LCP)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1057871921804736) != 0):
                self.state = 163
                self.stmt()
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 169
            self.match(HLangParser.RCP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(HLangParser.VardeclContext,0)


        def assignment(self):
            return self.getTypedRuleContext(HLangParser.AssignmentContext,0)


        def callstmt(self):
            return self.getTypedRuleContext(HLangParser.CallstmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(HLangParser.ReturnstmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(HLangParser.If_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(HLangParser.While_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(HLangParser.For_stmtContext,0)


        def exprstmt(self):
            return self.getTypedRuleContext(HLangParser.ExprstmtContext,0)


        def getRuleIndex(self):
            return HLangParser.RULE_stmt




    def stmt(self):

        localctx = HLangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_stmt)
        try:
            self.state = 179
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 173
                self.callstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 174
                self.returnstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 175
                self.if_stmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 176
                self.while_stmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 177
                self.for_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 178
                self.exprstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(HLangParser.FOR, 0)

        def LP(self):
            return self.getToken(HLangParser.LP, 0)

        def ID(self):
            return self.getToken(HLangParser.ID, 0)

        def IN(self):
            return self.getToken(HLangParser.IN, 0)

        def expr(self):
            return self.getTypedRuleContext(HLangParser.ExprContext,0)


        def RP(self):
            return self.getToken(HLangParser.RP, 0)

        def body(self):
            return self.getTypedRuleContext(HLangParser.BodyContext,0)


        def getRuleIndex(self):
            return HLangParser.RULE_for_stmt




    def for_stmt(self):

        localctx = HLangParser.For_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(HLangParser.FOR)
            self.state = 182
            self.match(HLangParser.LP)
            self.state = 183
            self.match(HLangParser.ID)
            self.state = 184
            self.match(HLangParser.IN)
            self.state = 185
            self.expr()
            self.state = 186
            self.match(HLangParser.RP)
            self.state = 187
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(HLangParser.WHILE, 0)

        def LP(self):
            return self.getToken(HLangParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(HLangParser.ExprContext,0)


        def RP(self):
            return self.getToken(HLangParser.RP, 0)

        def body(self):
            return self.getTypedRuleContext(HLangParser.BodyContext,0)


        def getRuleIndex(self):
            return HLangParser.RULE_while_stmt




    def while_stmt(self):

        localctx = HLangParser.While_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(HLangParser.WHILE)
            self.state = 190
            self.match(HLangParser.LP)
            self.state = 191
            self.expr()
            self.state = 192
            self.match(HLangParser.RP)
            self.state = 193
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(HLangParser.IF, 0)

        def LP(self):
            return self.getToken(HLangParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(HLangParser.ExprContext,0)


        def RP(self):
            return self.getToken(HLangParser.RP, 0)

        def body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HLangParser.BodyContext)
            else:
                return self.getTypedRuleContext(HLangParser.BodyContext,i)


        def ELSE(self):
            return self.getToken(HLangParser.ELSE, 0)

        def getRuleIndex(self):
            return HLangParser.RULE_if_stmt




    def if_stmt(self):

        localctx = HLangParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(HLangParser.IF)
            self.state = 196
            self.match(HLangParser.LP)
            self.state = 197
            self.expr()
            self.state = 198
            self.match(HLangParser.RP)
            self.state = 199
            self.body()
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 200
                self.match(HLangParser.ELSE)
                self.state = 201
                self.body()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(HLangParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(HLangParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(HLangParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(HLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return HLangParser.RULE_assignment




    def assignment(self):

        localctx = HLangParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.lhs()
            self.state = 205
            self.match(HLangParser.ASSIGN)
            self.state = 206
            self.expr()
            self.state = 207
            self.match(HLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(HLangParser.ID, 0)

        def LSP(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.LSP)
            else:
                return self.getToken(HLangParser.LSP, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(HLangParser.ExprContext,i)


        def RSP(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.RSP)
            else:
                return self.getToken(HLangParser.RSP, i)

        def getRuleIndex(self):
            return HLangParser.RULE_lhs




    def lhs(self):

        localctx = HLangParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_lhs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(HLangParser.ID)
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 210
                self.match(HLangParser.LSP)
                self.state = 211
                self.expr()
                self.state = 212
                self.match(HLangParser.RSP)
                self.state = 218
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def callexpr(self):
            return self.getTypedRuleContext(HLangParser.CallexprContext,0)


        def SEMICOLON(self):
            return self.getToken(HLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return HLangParser.RULE_callstmt




    def callstmt(self):

        localctx = HLangParser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.callexpr()
            self.state = 220
            self.match(HLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(HLangParser.RETURN, 0)

        def SEMICOLON(self):
            return self.getToken(HLangParser.SEMICOLON, 0)

        def expr(self):
            return self.getTypedRuleContext(HLangParser.ExprContext,0)


        def getRuleIndex(self):
            return HLangParser.RULE_returnstmt




    def returnstmt(self):

        localctx = HLangParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(HLangParser.RETURN)
            self.state = 224
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1057871921516736) != 0):
                self.state = 223
                self.expr()


            self.state = 226
            self.match(HLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(HLangParser.ExprContext,0)


        def SEMICOLON(self):
            return self.getToken(HLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return HLangParser.RULE_exprstmt




    def exprstmt(self):

        localctx = HLangParser.ExprstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_exprstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.expr()
            self.state = 229
            self.match(HLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(HLangParser.Expr1Context,0)


        def getRuleIndex(self):
            return HLangParser.RULE_expr




    def expr(self):

        localctx = HLangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.expr1(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HLangParser.RULE_expr1

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SingleOrContext(Expr1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HLangParser.Expr1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr2(self):
            return self.getTypedRuleContext(HLangParser.Expr2Context,0)



    class OrExprContext(Expr1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HLangParser.Expr1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr1(self):
            return self.getTypedRuleContext(HLangParser.Expr1Context,0)

        def OR(self):
            return self.getToken(HLangParser.OR, 0)
        def expr2(self):
            return self.getTypedRuleContext(HLangParser.Expr2Context,0)




    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HLangParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = HLangParser.SingleOrContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 234
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 241
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HLangParser.OrExprContext(self, HLangParser.Expr1Context(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 236
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 237
                    self.match(HLangParser.OR)
                    self.state = 238
                    self.expr2(0) 
                self.state = 243
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HLangParser.RULE_expr2

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AndExprContext(Expr2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HLangParser.Expr2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr2(self):
            return self.getTypedRuleContext(HLangParser.Expr2Context,0)

        def AND(self):
            return self.getToken(HLangParser.AND, 0)
        def expr3(self):
            return self.getTypedRuleContext(HLangParser.Expr3Context,0)



    class SingleAndContext(Expr2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HLangParser.Expr2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr3(self):
            return self.getTypedRuleContext(HLangParser.Expr3Context,0)




    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HLangParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = HLangParser.SingleAndContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 245
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 252
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HLangParser.AndExprContext(self, HLangParser.Expr2Context(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 247
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 248
                    self.match(HLangParser.AND)
                    self.state = 249
                    self.expr3(0) 
                self.state = 254
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HLangParser.RULE_expr3

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class EqualityExprContext(Expr3Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HLangParser.Expr3Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr3(self):
            return self.getTypedRuleContext(HLangParser.Expr3Context,0)

        def expr4(self):
            return self.getTypedRuleContext(HLangParser.Expr4Context,0)

        def EQUAL(self):
            return self.getToken(HLangParser.EQUAL, 0)
        def UNEQUAL(self):
            return self.getToken(HLangParser.UNEQUAL, 0)


    class SingleEqualityContext(Expr3Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HLangParser.Expr3Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr4(self):
            return self.getTypedRuleContext(HLangParser.Expr4Context,0)




    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HLangParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = HLangParser.SingleEqualityContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 256
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 263
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HLangParser.EqualityExprContext(self, HLangParser.Expr3Context(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 258
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 259
                    _la = self._input.LA(1)
                    if not(_la==24 or _la==25):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 260
                    self.expr4(0) 
                self.state = 265
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HLangParser.RULE_expr4

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class SingleRelationalContext(Expr4Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HLangParser.Expr4Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr5(self):
            return self.getTypedRuleContext(HLangParser.Expr5Context,0)



    class RelationalExprContext(Expr4Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HLangParser.Expr4Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr4(self):
            return self.getTypedRuleContext(HLangParser.Expr4Context,0)

        def expr5(self):
            return self.getTypedRuleContext(HLangParser.Expr5Context,0)

        def LT(self):
            return self.getToken(HLangParser.LT, 0)
        def LTE(self):
            return self.getToken(HLangParser.LTE, 0)
        def GT(self):
            return self.getToken(HLangParser.GT, 0)
        def GTE(self):
            return self.getToken(HLangParser.GTE, 0)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HLangParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = HLangParser.SingleRelationalContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 267
            self.expr5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 274
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HLangParser.RelationalExprContext(self, HLangParser.Expr4Context(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 269
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 270
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1006632960) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 271
                    self.expr5(0) 
                self.state = 276
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HLangParser.RULE_expr5

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class AdditiveExprContext(Expr5Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HLangParser.Expr5Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr5(self):
            return self.getTypedRuleContext(HLangParser.Expr5Context,0)

        def expr6(self):
            return self.getTypedRuleContext(HLangParser.Expr6Context,0)

        def ADD(self):
            return self.getToken(HLangParser.ADD, 0)
        def SUB(self):
            return self.getToken(HLangParser.SUB, 0)


    class SingleAdditiveContext(Expr5Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HLangParser.Expr5Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr6(self):
            return self.getTypedRuleContext(HLangParser.Expr6Context,0)




    def expr5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HLangParser.Expr5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_expr5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = HLangParser.SingleAdditiveContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 278
            self.expr6(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 285
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HLangParser.AdditiveExprContext(self, HLangParser.Expr5Context(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                    self.state = 280
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 281
                    _la = self._input.LA(1)
                    if not(_la==19 or _la==20):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 282
                    self.expr6(0) 
                self.state = 287
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HLangParser.RULE_expr6

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MultiplicativeExprContext(Expr6Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HLangParser.Expr6Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr6(self):
            return self.getTypedRuleContext(HLangParser.Expr6Context,0)

        def expr7(self):
            return self.getTypedRuleContext(HLangParser.Expr7Context,0)

        def MUL(self):
            return self.getToken(HLangParser.MUL, 0)
        def DIV(self):
            return self.getToken(HLangParser.DIV, 0)
        def MOD(self):
            return self.getToken(HLangParser.MOD, 0)


    class SingleMultiplicativeContext(Expr6Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HLangParser.Expr6Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr7(self):
            return self.getTypedRuleContext(HLangParser.Expr7Context,0)




    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HLangParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_expr6, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = HLangParser.SingleMultiplicativeContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 289
            self.expr7(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 296
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HLangParser.MultiplicativeExprContext(self, HLangParser.Expr6Context(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                    self.state = 291
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 292
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14680064) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 293
                    self.expr7(0) 
                self.state = 298
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HLangParser.RULE_expr7

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class PipelineExprContext(Expr7Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HLangParser.Expr7Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr7(self):
            return self.getTypedRuleContext(HLangParser.Expr7Context,0)

        def PIPELINE(self):
            return self.getToken(HLangParser.PIPELINE, 0)
        def expr8(self):
            return self.getTypedRuleContext(HLangParser.Expr8Context,0)



    class SinglePipelineContext(Expr7Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HLangParser.Expr7Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr8(self):
            return self.getTypedRuleContext(HLangParser.Expr8Context,0)




    def expr7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HLangParser.Expr7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = HLangParser.SinglePipelineContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 300
            self.expr8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 307
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HLangParser.PipelineExprContext(self, HLangParser.Expr7Context(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 302
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 303
                    self.match(HLangParser.PIPELINE)
                    self.state = 304
                    self.expr8() 
                self.state = 309
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HLangParser.RULE_expr8

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SinglePostfixContext(Expr8Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HLangParser.Expr8Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr9(self):
            return self.getTypedRuleContext(HLangParser.Expr9Context,0)



    class UnaryExprContext(Expr8Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HLangParser.Expr8Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr8(self):
            return self.getTypedRuleContext(HLangParser.Expr8Context,0)

        def NOT(self):
            return self.getToken(HLangParser.NOT, 0)
        def SUB(self):
            return self.getToken(HLangParser.SUB, 0)
        def ADD(self):
            return self.getToken(HLangParser.ADD, 0)



    def expr8(self):

        localctx = HLangParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_expr8)
        self._la = 0 # Token type
        try:
            self.state = 313
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 20, 32]:
                localctx = HLangParser.UnaryExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 310
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4296540160) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 311
                self.expr8()
                pass
            elif token in [6, 7, 12, 15, 16, 37, 41, 46, 47, 48, 49]:
                localctx = HLangParser.SinglePostfixContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 312
                self.expr9()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HLangParser.RULE_expr9

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PostfixExprContext(Expr9Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HLangParser.Expr9Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def primary_expr(self):
            return self.getTypedRuleContext(HLangParser.Primary_exprContext,0)

        def LSP(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.LSP)
            else:
                return self.getToken(HLangParser.LSP, i)
        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(HLangParser.ExprContext,i)

        def RSP(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.RSP)
            else:
                return self.getToken(HLangParser.RSP, i)



    def expr9(self):

        localctx = HLangParser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_expr9)
        try:
            localctx = HLangParser.PostfixExprContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 315
            self.primary_expr()
            self.state = 322
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 316
                    self.match(HLangParser.LSP)
                    self.state = 317
                    self.expr()
                    self.state = 318
                    self.match(HLangParser.RSP) 
                self.state = 324
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primary_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(HLangParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(HLangParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(HLangParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(HLangParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(HLangParser.FALSE, 0)

        def array_lit(self):
            return self.getTypedRuleContext(HLangParser.Array_litContext,0)


        def callexpr(self):
            return self.getTypedRuleContext(HLangParser.CallexprContext,0)


        def ID(self):
            return self.getToken(HLangParser.ID, 0)

        def LP(self):
            return self.getToken(HLangParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(HLangParser.ExprContext,0)


        def RP(self):
            return self.getToken(HLangParser.RP, 0)

        def getRuleIndex(self):
            return HLangParser.RULE_primary_expr




    def primary_expr(self):

        localctx = HLangParser.Primary_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_primary_expr)
        try:
            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 325
                self.match(HLangParser.INT_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
                self.match(HLangParser.FLOAT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 327
                self.match(HLangParser.STRING_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 328
                self.match(HLangParser.TRUE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 329
                self.match(HLangParser.FALSE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 330
                self.array_lit()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 331
                self.callexpr()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 332
                self.match(HLangParser.ID)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 333
                self.match(HLangParser.LP)
                self.state = 334
                self.expr()
                self.state = 335
                self.match(HLangParser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def callee(self):
            return self.getTypedRuleContext(HLangParser.CalleeContext,0)


        def LP(self):
            return self.getToken(HLangParser.LP, 0)

        def exprlist(self):
            return self.getTypedRuleContext(HLangParser.ExprlistContext,0)


        def RP(self):
            return self.getToken(HLangParser.RP, 0)

        def getRuleIndex(self):
            return HLangParser.RULE_callexpr




    def callexpr(self):

        localctx = HLangParser.CallexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_callexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.callee()
            self.state = 340
            self.match(HLangParser.LP)
            self.state = 341
            self.exprlist()
            self.state = 342
            self.match(HLangParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CalleeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(HLangParser.ID, 0)

        def builtin_func(self):
            return self.getTypedRuleContext(HLangParser.Builtin_funcContext,0)


        def getRuleIndex(self):
            return HLangParser.RULE_callee




    def callee(self):

        localctx = HLangParser.CalleeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_callee)
        try:
            self.state = 346
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 344
                self.match(HLangParser.ID)
                pass
            elif token in [7, 12, 15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 345
                self.builtin_func()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Builtin_funcContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(HLangParser.INT, 0)

        def FLOAT(self):
            return self.getToken(HLangParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(HLangParser.STRING, 0)

        def getRuleIndex(self):
            return HLangParser.RULE_builtin_func




    def builtin_func(self):

        localctx = HLangParser.Builtin_funcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_builtin_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 36992) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_litContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSP(self):
            return self.getToken(HLangParser.LSP, 0)

        def exprlist(self):
            return self.getTypedRuleContext(HLangParser.ExprlistContext,0)


        def RSP(self):
            return self.getToken(HLangParser.RSP, 0)

        def getRuleIndex(self):
            return HLangParser.RULE_array_lit




    def array_lit(self):

        localctx = HLangParser.Array_litContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(HLangParser.LSP)
            self.state = 351
            self.exprlist()
            self.state = 352
            self.match(HLangParser.RSP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HLangParser.ExprContext)
            else:
                return self.getTypedRuleContext(HLangParser.ExprContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(HLangParser.COMMA)
            else:
                return self.getToken(HLangParser.COMMA, i)

        def getRuleIndex(self):
            return HLangParser.RULE_exprlist




    def exprlist(self):

        localctx = HLangParser.ExprlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_exprlist)
        self._la = 0 # Token type
        try:
            self.state = 363
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7, 12, 15, 16, 19, 20, 32, 37, 41, 46, 47, 48, 49]:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.expr()
                self.state = 359
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==43:
                    self.state = 355
                    self.match(HLangParser.COMMA)
                    self.state = 356
                    self.expr()
                    self.state = 361
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [38, 42]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[24] = self.expr1_sempred
        self._predicates[25] = self.expr2_sempred
        self._predicates[26] = self.expr3_sempred
        self._predicates[27] = self.expr4_sempred
        self._predicates[28] = self.expr5_sempred
        self._predicates[29] = self.expr6_sempred
        self._predicates[30] = self.expr7_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr5_sempred(self, localctx:Expr5Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr6_sempred(self, localctx:Expr6Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def expr7_sempred(self, localctx:Expr7Context, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




