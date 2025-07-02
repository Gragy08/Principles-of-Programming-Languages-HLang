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
        4,1,57,406,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,1,0,5,0,84,8,0,10,0,12,0,87,9,0,1,0,5,0,90,8,0,10,0,12,
        0,93,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,101,8,1,1,1,1,1,1,1,1,1,1,2,
        1,2,1,2,1,2,3,2,111,8,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,4,1,4,1,5,1,5,3,5,128,8,5,1,6,1,6,1,6,1,6,1,6,3,6,135,8,6,
        1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,5,8,146,8,8,10,8,12,8,149,9,
        8,1,9,1,9,3,9,153,8,9,1,9,1,9,1,10,1,10,1,10,5,10,160,8,10,10,10,
        12,10,163,9,10,1,11,1,11,1,11,1,11,1,12,1,12,5,12,171,8,12,10,12,
        12,12,174,9,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,3,13,189,8,13,1,14,1,14,1,14,1,15,1,15,1,15,1,16,
        1,16,5,16,199,8,16,10,16,12,16,202,9,16,1,16,1,16,1,17,1,17,1,17,
        1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,
        1,19,1,19,1,19,1,19,1,19,3,19,227,8,19,1,20,1,20,3,20,231,8,20,1,
        21,1,21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,5,22,243,8,22,10,
        22,12,22,246,9,22,1,23,1,23,1,23,1,24,1,24,3,24,253,8,24,1,24,1,
        24,1,25,1,25,1,25,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,27,5,27,268,
        8,27,10,27,12,27,271,9,27,1,28,1,28,1,28,1,28,1,28,1,28,5,28,279,
        8,28,10,28,12,28,282,9,28,1,29,1,29,1,29,1,29,1,29,1,29,5,29,290,
        8,29,10,29,12,29,293,9,29,1,30,1,30,1,30,1,30,1,30,1,30,5,30,301,
        8,30,10,30,12,30,304,9,30,1,31,1,31,1,31,1,31,1,31,1,31,5,31,312,
        8,31,10,31,12,31,315,9,31,1,32,1,32,1,32,1,32,1,32,1,32,5,32,323,
        8,32,10,32,12,32,326,9,32,1,33,1,33,1,33,1,33,1,33,1,33,5,33,334,
        8,33,10,33,12,33,337,9,33,1,34,1,34,1,34,3,34,342,8,34,1,35,1,35,
        1,35,1,35,1,35,5,35,349,8,35,10,35,12,35,352,9,35,1,36,1,36,1,36,
        1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,1,36,3,36,367,8,36,
        1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,
        1,37,1,37,3,37,384,8,37,1,38,1,38,1,38,1,38,1,38,1,39,1,39,1,39,
        1,39,1,40,1,40,1,40,5,40,398,8,40,10,40,12,40,401,9,40,1,40,3,40,
        404,8,40,1,40,0,7,54,56,58,60,62,64,66,41,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,
        62,64,66,68,70,72,74,76,78,80,0,5,1,0,25,26,1,0,27,30,1,0,20,21,
        1,0,22,24,2,0,20,21,33,33,414,0,85,1,0,0,0,2,96,1,0,0,0,4,106,1,
        0,0,0,6,116,1,0,0,0,8,123,1,0,0,0,10,127,1,0,0,0,12,134,1,0,0,0,
        14,136,1,0,0,0,16,142,1,0,0,0,18,150,1,0,0,0,20,156,1,0,0,0,22,164,
        1,0,0,0,24,168,1,0,0,0,26,188,1,0,0,0,28,190,1,0,0,0,30,193,1,0,
        0,0,32,196,1,0,0,0,34,205,1,0,0,0,36,213,1,0,0,0,38,219,1,0,0,0,
        40,230,1,0,0,0,42,232,1,0,0,0,44,237,1,0,0,0,46,247,1,0,0,0,48,250,
        1,0,0,0,50,256,1,0,0,0,52,259,1,0,0,0,54,261,1,0,0,0,56,272,1,0,
        0,0,58,283,1,0,0,0,60,294,1,0,0,0,62,305,1,0,0,0,64,316,1,0,0,0,
        66,327,1,0,0,0,68,341,1,0,0,0,70,343,1,0,0,0,72,366,1,0,0,0,74,383,
        1,0,0,0,76,385,1,0,0,0,78,390,1,0,0,0,80,403,1,0,0,0,82,84,3,2,1,
        0,83,82,1,0,0,0,84,87,1,0,0,0,85,83,1,0,0,0,85,86,1,0,0,0,86,91,
        1,0,0,0,87,85,1,0,0,0,88,90,3,6,3,0,89,88,1,0,0,0,90,93,1,0,0,0,
        91,89,1,0,0,0,91,92,1,0,0,0,92,94,1,0,0,0,93,91,1,0,0,0,94,95,5,
        0,0,1,95,1,1,0,0,0,96,97,5,3,0,0,97,100,5,47,0,0,98,99,5,35,0,0,
        99,101,3,8,4,0,100,98,1,0,0,0,100,101,1,0,0,0,101,102,1,0,0,0,102,
        103,5,34,0,0,103,104,3,52,26,0,104,105,5,45,0,0,105,3,1,0,0,0,106,
        107,5,13,0,0,107,110,5,47,0,0,108,109,5,35,0,0,109,111,3,8,4,0,110,
        108,1,0,0,0,110,111,1,0,0,0,111,112,1,0,0,0,112,113,5,34,0,0,113,
        114,3,52,26,0,114,115,5,45,0,0,115,5,1,0,0,0,116,117,5,9,0,0,117,
        118,5,47,0,0,118,119,3,18,9,0,119,120,5,36,0,0,120,121,3,10,5,0,
        121,122,3,24,12,0,122,7,1,0,0,0,123,124,3,12,6,0,124,9,1,0,0,0,125,
        128,3,12,6,0,126,128,5,18,0,0,127,125,1,0,0,0,127,126,1,0,0,0,128,
        11,1,0,0,0,129,135,5,12,0,0,130,135,5,7,0,0,131,135,5,1,0,0,132,
        135,5,15,0,0,133,135,3,14,7,0,134,129,1,0,0,0,134,130,1,0,0,0,134,
        131,1,0,0,0,134,132,1,0,0,0,134,133,1,0,0,0,135,13,1,0,0,0,136,137,
        5,42,0,0,137,138,3,12,6,0,138,139,5,45,0,0,139,140,5,48,0,0,140,
        141,5,43,0,0,141,15,1,0,0,0,142,147,5,47,0,0,143,144,5,44,0,0,144,
        146,5,47,0,0,145,143,1,0,0,0,146,149,1,0,0,0,147,145,1,0,0,0,147,
        148,1,0,0,0,148,17,1,0,0,0,149,147,1,0,0,0,150,152,5,38,0,0,151,
        153,3,20,10,0,152,151,1,0,0,0,152,153,1,0,0,0,153,154,1,0,0,0,154,
        155,5,39,0,0,155,19,1,0,0,0,156,161,3,22,11,0,157,158,5,44,0,0,158,
        160,3,22,11,0,159,157,1,0,0,0,160,163,1,0,0,0,161,159,1,0,0,0,161,
        162,1,0,0,0,162,21,1,0,0,0,163,161,1,0,0,0,164,165,5,47,0,0,165,
        166,5,35,0,0,166,167,3,8,4,0,167,23,1,0,0,0,168,172,5,40,0,0,169,
        171,3,26,13,0,170,169,1,0,0,0,171,174,1,0,0,0,172,170,1,0,0,0,172,
        173,1,0,0,0,173,175,1,0,0,0,174,172,1,0,0,0,175,176,5,41,0,0,176,
        25,1,0,0,0,177,189,3,4,2,0,178,189,3,42,21,0,179,189,3,46,23,0,180,
        189,3,48,24,0,181,189,3,28,14,0,182,189,3,30,15,0,183,189,3,38,19,
        0,184,189,3,36,18,0,185,189,3,34,17,0,186,189,3,50,25,0,187,189,
        3,32,16,0,188,177,1,0,0,0,188,178,1,0,0,0,188,179,1,0,0,0,188,180,
        1,0,0,0,188,181,1,0,0,0,188,182,1,0,0,0,188,183,1,0,0,0,188,184,
        1,0,0,0,188,185,1,0,0,0,188,186,1,0,0,0,188,187,1,0,0,0,189,27,1,
        0,0,0,190,191,5,2,0,0,191,192,5,45,0,0,192,29,1,0,0,0,193,194,5,
        4,0,0,194,195,5,45,0,0,195,31,1,0,0,0,196,200,5,40,0,0,197,199,3,
        26,13,0,198,197,1,0,0,0,199,202,1,0,0,0,200,198,1,0,0,0,200,201,
        1,0,0,0,201,203,1,0,0,0,202,200,1,0,0,0,203,204,5,41,0,0,204,33,
        1,0,0,0,205,206,5,8,0,0,206,207,5,38,0,0,207,208,5,47,0,0,208,209,
        5,11,0,0,209,210,3,52,26,0,210,211,5,39,0,0,211,212,3,24,12,0,212,
        35,1,0,0,0,213,214,5,19,0,0,214,215,5,38,0,0,215,216,3,52,26,0,216,
        217,5,39,0,0,217,218,3,24,12,0,218,37,1,0,0,0,219,220,5,10,0,0,220,
        221,5,38,0,0,221,222,3,52,26,0,222,223,5,39,0,0,223,226,3,24,12,
        0,224,225,5,5,0,0,225,227,3,40,20,0,226,224,1,0,0,0,226,227,1,0,
        0,0,227,39,1,0,0,0,228,231,3,38,19,0,229,231,3,24,12,0,230,228,1,
        0,0,0,230,229,1,0,0,0,231,41,1,0,0,0,232,233,3,44,22,0,233,234,5,
        34,0,0,234,235,3,52,26,0,235,236,5,45,0,0,236,43,1,0,0,0,237,244,
        5,47,0,0,238,239,5,42,0,0,239,240,3,52,26,0,240,241,5,43,0,0,241,
        243,1,0,0,0,242,238,1,0,0,0,243,246,1,0,0,0,244,242,1,0,0,0,244,
        245,1,0,0,0,245,45,1,0,0,0,246,244,1,0,0,0,247,248,3,76,38,0,248,
        249,5,45,0,0,249,47,1,0,0,0,250,252,5,14,0,0,251,253,3,52,26,0,252,
        251,1,0,0,0,252,253,1,0,0,0,253,254,1,0,0,0,254,255,5,45,0,0,255,
        49,1,0,0,0,256,257,3,52,26,0,257,258,5,45,0,0,258,51,1,0,0,0,259,
        260,3,54,27,0,260,53,1,0,0,0,261,262,6,27,-1,0,262,263,3,56,28,0,
        263,269,1,0,0,0,264,265,10,2,0,0,265,266,5,32,0,0,266,268,3,56,28,
        0,267,264,1,0,0,0,268,271,1,0,0,0,269,267,1,0,0,0,269,270,1,0,0,
        0,270,55,1,0,0,0,271,269,1,0,0,0,272,273,6,28,-1,0,273,274,3,58,
        29,0,274,280,1,0,0,0,275,276,10,2,0,0,276,277,5,31,0,0,277,279,3,
        58,29,0,278,275,1,0,0,0,279,282,1,0,0,0,280,278,1,0,0,0,280,281,
        1,0,0,0,281,57,1,0,0,0,282,280,1,0,0,0,283,284,6,29,-1,0,284,285,
        3,60,30,0,285,291,1,0,0,0,286,287,10,2,0,0,287,288,7,0,0,0,288,290,
        3,60,30,0,289,286,1,0,0,0,290,293,1,0,0,0,291,289,1,0,0,0,291,292,
        1,0,0,0,292,59,1,0,0,0,293,291,1,0,0,0,294,295,6,30,-1,0,295,296,
        3,62,31,0,296,302,1,0,0,0,297,298,10,2,0,0,298,299,7,1,0,0,299,301,
        3,62,31,0,300,297,1,0,0,0,301,304,1,0,0,0,302,300,1,0,0,0,302,303,
        1,0,0,0,303,61,1,0,0,0,304,302,1,0,0,0,305,306,6,31,-1,0,306,307,
        3,64,32,0,307,313,1,0,0,0,308,309,10,2,0,0,309,310,7,2,0,0,310,312,
        3,64,32,0,311,308,1,0,0,0,312,315,1,0,0,0,313,311,1,0,0,0,313,314,
        1,0,0,0,314,63,1,0,0,0,315,313,1,0,0,0,316,317,6,32,-1,0,317,318,
        3,66,33,0,318,324,1,0,0,0,319,320,10,2,0,0,320,321,7,3,0,0,321,323,
        3,66,33,0,322,319,1,0,0,0,323,326,1,0,0,0,324,322,1,0,0,0,324,325,
        1,0,0,0,325,65,1,0,0,0,326,324,1,0,0,0,327,328,6,33,-1,0,328,329,
        3,68,34,0,329,335,1,0,0,0,330,331,10,2,0,0,331,332,5,37,0,0,332,
        334,3,68,34,0,333,330,1,0,0,0,334,337,1,0,0,0,335,333,1,0,0,0,335,
        336,1,0,0,0,336,67,1,0,0,0,337,335,1,0,0,0,338,339,7,4,0,0,339,342,
        3,68,34,0,340,342,3,70,35,0,341,338,1,0,0,0,341,340,1,0,0,0,342,
        69,1,0,0,0,343,350,3,72,36,0,344,345,5,42,0,0,345,346,3,52,26,0,
        346,347,5,43,0,0,347,349,1,0,0,0,348,344,1,0,0,0,349,352,1,0,0,0,
        350,348,1,0,0,0,350,351,1,0,0,0,351,71,1,0,0,0,352,350,1,0,0,0,353,
        367,5,48,0,0,354,367,5,49,0,0,355,367,5,50,0,0,356,367,5,17,0,0,
        357,367,5,6,0,0,358,367,3,78,39,0,359,367,3,74,37,0,360,367,3,76,
        38,0,361,367,5,47,0,0,362,363,5,38,0,0,363,364,3,52,26,0,364,365,
        5,39,0,0,365,367,1,0,0,0,366,353,1,0,0,0,366,354,1,0,0,0,366,355,
        1,0,0,0,366,356,1,0,0,0,366,357,1,0,0,0,366,358,1,0,0,0,366,359,
        1,0,0,0,366,360,1,0,0,0,366,361,1,0,0,0,366,362,1,0,0,0,367,73,1,
        0,0,0,368,369,5,12,0,0,369,370,5,38,0,0,370,371,3,80,40,0,371,372,
        5,39,0,0,372,384,1,0,0,0,373,374,5,7,0,0,374,375,5,38,0,0,375,376,
        3,80,40,0,376,377,5,39,0,0,377,384,1,0,0,0,378,379,5,16,0,0,379,
        380,5,38,0,0,380,381,3,80,40,0,381,382,5,39,0,0,382,384,1,0,0,0,
        383,368,1,0,0,0,383,373,1,0,0,0,383,378,1,0,0,0,384,75,1,0,0,0,385,
        386,5,47,0,0,386,387,5,38,0,0,387,388,3,80,40,0,388,389,5,39,0,0,
        389,77,1,0,0,0,390,391,5,42,0,0,391,392,3,80,40,0,392,393,5,43,0,
        0,393,79,1,0,0,0,394,399,3,52,26,0,395,396,5,44,0,0,396,398,3,52,
        26,0,397,395,1,0,0,0,398,401,1,0,0,0,399,397,1,0,0,0,399,400,1,0,
        0,0,400,404,1,0,0,0,401,399,1,0,0,0,402,404,1,0,0,0,403,394,1,0,
        0,0,403,402,1,0,0,0,404,81,1,0,0,0,29,85,91,100,110,127,134,147,
        152,161,172,188,200,226,230,244,252,269,280,291,302,313,324,335,
        341,350,366,383,399,403
    ]

class HLangParser ( Parser ):

    grammarFileName = "HLang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'bool'", "'break'", "'const'", "'continue'", 
                     "'else'", "'false'", "'float'", "'for'", "'func'", 
                     "'if'", "'in'", "'int'", "'let'", "'return'", "'string'", 
                     "'str'", "'true'", "'void'", "'while'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'=='", "'!='", "'<'", "'<='", 
                     "'>'", "'>='", "'&&'", "'||'", "'!'", "'='", "':'", 
                     "'->'", "'>>'", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "','", "';'", "'.'" ]

    symbolicNames = [ "<INVALID>", "BOOL", "BREAK", "CONST", "CONTINUE", 
                      "ELSE", "FALSE", "FLOAT", "FOR", "FUNC", "IF", "IN", 
                      "INT", "LET", "RETURN", "STRING", "STR", "TRUE", "VOID", 
                      "WHILE", "ADD", "SUB", "MUL", "DIV", "MOD", "EQUAL", 
                      "UNEQUAL", "LT", "LTE", "GT", "GTE", "AND", "OR", 
                      "NOT", "ASSIGN", "COLON", "ARROW", "PIPELINE", "LP", 
                      "RP", "LCP", "RCP", "LSP", "RSP", "COMMA", "SEMICOLON", 
                      "DOT", "ID", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
                      "WS", "NEWLINE", "COMMENT_LINE", "COMMENT", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_constdecl = 1
    RULE_vardecl = 2
    RULE_funcdecl = 3
    RULE_var_type = 4
    RULE_ret_type = 5
    RULE_non_void_type = 6
    RULE_array_type = 7
    RULE_idlist = 8
    RULE_paramdecl = 9
    RULE_paramlist = 10
    RULE_param = 11
    RULE_body = 12
    RULE_stmt = 13
    RULE_breakstmt = 14
    RULE_continuestmt = 15
    RULE_blockstmt = 16
    RULE_for_stmt = 17
    RULE_while_stmt = 18
    RULE_if_stmt = 19
    RULE_else_stmt = 20
    RULE_assignment = 21
    RULE_lhs = 22
    RULE_callstmt = 23
    RULE_returnstmt = 24
    RULE_exprstmt = 25
    RULE_expr = 26
    RULE_expr1 = 27
    RULE_expr2 = 28
    RULE_expr3 = 29
    RULE_expr4 = 30
    RULE_expr5 = 31
    RULE_expr6 = 32
    RULE_expr7 = 33
    RULE_expr8 = 34
    RULE_expr9 = 35
    RULE_primary_expr = 36
    RULE_type_conversion_call = 37
    RULE_callexpr = 38
    RULE_array_lit = 39
    RULE_exprlist = 40

    ruleNames =  [ "program", "constdecl", "vardecl", "funcdecl", "var_type", 
                   "ret_type", "non_void_type", "array_type", "idlist", 
                   "paramdecl", "paramlist", "param", "body", "stmt", "breakstmt", 
                   "continuestmt", "blockstmt", "for_stmt", "while_stmt", 
                   "if_stmt", "else_stmt", "assignment", "lhs", "callstmt", 
                   "returnstmt", "exprstmt", "expr", "expr1", "expr2", "expr3", 
                   "expr4", "expr5", "expr6", "expr7", "expr8", "expr9", 
                   "primary_expr", "type_conversion_call", "callexpr", "array_lit", 
                   "exprlist" ]

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
    STR=16
    TRUE=17
    VOID=18
    WHILE=19
    ADD=20
    SUB=21
    MUL=22
    DIV=23
    MOD=24
    EQUAL=25
    UNEQUAL=26
    LT=27
    LTE=28
    GT=29
    GTE=30
    AND=31
    OR=32
    NOT=33
    ASSIGN=34
    COLON=35
    ARROW=36
    PIPELINE=37
    LP=38
    RP=39
    LCP=40
    RCP=41
    LSP=42
    RSP=43
    COMMA=44
    SEMICOLON=45
    DOT=46
    ID=47
    INT_LIT=48
    FLOAT_LIT=49
    STRING_LIT=50
    WS=51
    NEWLINE=52
    COMMENT_LINE=53
    COMMENT=54
    UNCLOSE_STRING=55
    ILLEGAL_ESCAPE=56
    ERROR_CHAR=57

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

        def constdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HLangParser.ConstdeclContext)
            else:
                return self.getTypedRuleContext(HLangParser.ConstdeclContext,i)


        def funcdecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HLangParser.FuncdeclContext)
            else:
                return self.getTypedRuleContext(HLangParser.FuncdeclContext,i)


        def getRuleIndex(self):
            return HLangParser.RULE_program




    def program(self):

        localctx = HLangParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 82
                self.constdecl()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 91
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9:
                self.state = 88
                self.funcdecl()
                self.state = 93
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 94
            self.match(HLangParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_constdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(HLangParser.CONST)
            self.state = 97
            self.match(HLangParser.ID)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 98
                self.match(HLangParser.COLON)
                self.state = 99
                self.var_type()


            self.state = 102
            self.match(HLangParser.ASSIGN)
            self.state = 103
            self.expr()
            self.state = 104
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
        self.enterRule(localctx, 4, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(HLangParser.LET)
            self.state = 107
            self.match(HLangParser.ID)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 108
                self.match(HLangParser.COLON)
                self.state = 109
                self.var_type()


            self.state = 112
            self.match(HLangParser.ASSIGN)
            self.state = 113
            self.expr()
            self.state = 114
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
        self.enterRule(localctx, 6, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(HLangParser.FUNC)
            self.state = 117
            self.match(HLangParser.ID)
            self.state = 118
            self.paramdecl()
            self.state = 119
            self.match(HLangParser.ARROW)
            self.state = 120
            self.ret_type()
            self.state = 121
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
        self.enterRule(localctx, 8, self.RULE_var_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
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
        self.enterRule(localctx, 10, self.RULE_ret_type)
        try:
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 7, 12, 15, 42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 125
                self.non_void_type()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 126
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
        self.enterRule(localctx, 12, self.RULE_non_void_type)
        try:
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 129
                self.match(HLangParser.INT)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 130
                self.match(HLangParser.FLOAT)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 131
                self.match(HLangParser.BOOL)
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 4)
                self.state = 132
                self.match(HLangParser.STRING)
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 5)
                self.state = 133
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
        self.enterRule(localctx, 14, self.RULE_array_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(HLangParser.LSP)
            self.state = 137
            self.non_void_type()
            self.state = 138
            self.match(HLangParser.SEMICOLON)
            self.state = 139
            self.match(HLangParser.INT_LIT)
            self.state = 140
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
        self.enterRule(localctx, 16, self.RULE_idlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            self.match(HLangParser.ID)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==44:
                self.state = 143
                self.match(HLangParser.COMMA)
                self.state = 144
                self.match(HLangParser.ID)
                self.state = 149
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
        self.enterRule(localctx, 18, self.RULE_paramdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(HLangParser.LP)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47:
                self.state = 151
                self.paramlist()


            self.state = 154
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
        self.enterRule(localctx, 20, self.RULE_paramlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.param()
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==44:
                self.state = 157
                self.match(HLangParser.COMMA)
                self.state = 158
                self.param()
                self.state = 163
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
        self.enterRule(localctx, 22, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(HLangParser.ID)
            self.state = 165
            self.match(HLangParser.COLON)
            self.state = 166
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
        self.enterRule(localctx, 24, self.RULE_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            self.match(HLangParser.LCP)
            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2116843355207124) != 0):
                self.state = 169
                self.stmt()
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 175
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


        def breakstmt(self):
            return self.getTypedRuleContext(HLangParser.BreakstmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(HLangParser.ContinuestmtContext,0)


        def if_stmt(self):
            return self.getTypedRuleContext(HLangParser.If_stmtContext,0)


        def while_stmt(self):
            return self.getTypedRuleContext(HLangParser.While_stmtContext,0)


        def for_stmt(self):
            return self.getTypedRuleContext(HLangParser.For_stmtContext,0)


        def exprstmt(self):
            return self.getTypedRuleContext(HLangParser.ExprstmtContext,0)


        def blockstmt(self):
            return self.getTypedRuleContext(HLangParser.BlockstmtContext,0)


        def getRuleIndex(self):
            return HLangParser.RULE_stmt




    def stmt(self):

        localctx = HLangParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_stmt)
        try:
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.assignment()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 179
                self.callstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 180
                self.returnstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 181
                self.breakstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 182
                self.continuestmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 183
                self.if_stmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 184
                self.while_stmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 185
                self.for_stmt()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 186
                self.exprstmt()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 187
                self.blockstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(HLangParser.BREAK, 0)

        def SEMICOLON(self):
            return self.getToken(HLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return HLangParser.RULE_breakstmt




    def breakstmt(self):

        localctx = HLangParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(HLangParser.BREAK)
            self.state = 191
            self.match(HLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(HLangParser.CONTINUE, 0)

        def SEMICOLON(self):
            return self.getToken(HLangParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return HLangParser.RULE_continuestmt




    def continuestmt(self):

        localctx = HLangParser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(HLangParser.CONTINUE)
            self.state = 194
            self.match(HLangParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockstmtContext(ParserRuleContext):
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
            return HLangParser.RULE_blockstmt




    def blockstmt(self):

        localctx = HLangParser.BlockstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_blockstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.match(HLangParser.LCP)
            self.state = 200
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2116843355207124) != 0):
                self.state = 197
                self.stmt()
                self.state = 202
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 203
            self.match(HLangParser.RCP)
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
        self.enterRule(localctx, 34, self.RULE_for_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(HLangParser.FOR)
            self.state = 206
            self.match(HLangParser.LP)
            self.state = 207
            self.match(HLangParser.ID)
            self.state = 208
            self.match(HLangParser.IN)
            self.state = 209
            self.expr()
            self.state = 210
            self.match(HLangParser.RP)
            self.state = 211
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
        self.enterRule(localctx, 36, self.RULE_while_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(HLangParser.WHILE)
            self.state = 214
            self.match(HLangParser.LP)
            self.state = 215
            self.expr()
            self.state = 216
            self.match(HLangParser.RP)
            self.state = 217
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

        def body(self):
            return self.getTypedRuleContext(HLangParser.BodyContext,0)


        def ELSE(self):
            return self.getToken(HLangParser.ELSE, 0)

        def else_stmt(self):
            return self.getTypedRuleContext(HLangParser.Else_stmtContext,0)


        def getRuleIndex(self):
            return HLangParser.RULE_if_stmt




    def if_stmt(self):

        localctx = HLangParser.If_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_if_stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(HLangParser.IF)
            self.state = 220
            self.match(HLangParser.LP)
            self.state = 221
            self.expr()
            self.state = 222
            self.match(HLangParser.RP)
            self.state = 223
            self.body()
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 224
                self.match(HLangParser.ELSE)
                self.state = 225
                self.else_stmt()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Else_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_stmt(self):
            return self.getTypedRuleContext(HLangParser.If_stmtContext,0)


        def body(self):
            return self.getTypedRuleContext(HLangParser.BodyContext,0)


        def getRuleIndex(self):
            return HLangParser.RULE_else_stmt




    def else_stmt(self):

        localctx = HLangParser.Else_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_else_stmt)
        try:
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 228
                self.if_stmt()
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
                self.body()
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
        self.enterRule(localctx, 42, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.lhs()
            self.state = 233
            self.match(HLangParser.ASSIGN)
            self.state = 234
            self.expr()
            self.state = 235
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
        self.enterRule(localctx, 44, self.RULE_lhs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(HLangParser.ID)
            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==42:
                self.state = 238
                self.match(HLangParser.LSP)
                self.state = 239
                self.expr()
                self.state = 240
                self.match(HLangParser.RSP)
                self.state = 246
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
        self.enterRule(localctx, 46, self.RULE_callstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.callexpr()
            self.state = 248
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
        self.enterRule(localctx, 48, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.match(HLangParser.RETURN)
            self.state = 252
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2115743843029184) != 0):
                self.state = 251
                self.expr()


            self.state = 254
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
        self.enterRule(localctx, 50, self.RULE_exprstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.expr()
            self.state = 257
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
        self.enterRule(localctx, 52, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
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

        def expr2(self):
            return self.getTypedRuleContext(HLangParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(HLangParser.Expr1Context,0)


        def OR(self):
            return self.getToken(HLangParser.OR, 0)

        def getRuleIndex(self):
            return HLangParser.RULE_expr1



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HLangParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 269
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HLangParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 264
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 265
                    self.match(HLangParser.OR)
                    self.state = 266
                    self.expr2(0) 
                self.state = 271
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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

        def expr3(self):
            return self.getTypedRuleContext(HLangParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(HLangParser.Expr2Context,0)


        def AND(self):
            return self.getToken(HLangParser.AND, 0)

        def getRuleIndex(self):
            return HLangParser.RULE_expr2



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HLangParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_expr2, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 273
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 280
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HLangParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 275
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 276
                    self.match(HLangParser.AND)
                    self.state = 277
                    self.expr3(0) 
                self.state = 282
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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

        def expr4(self):
            return self.getTypedRuleContext(HLangParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(HLangParser.Expr3Context,0)


        def EQUAL(self):
            return self.getToken(HLangParser.EQUAL, 0)

        def UNEQUAL(self):
            return self.getToken(HLangParser.UNEQUAL, 0)

        def getRuleIndex(self):
            return HLangParser.RULE_expr3



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HLangParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HLangParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 286
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 287
                    _la = self._input.LA(1)
                    if not(_la==25 or _la==26):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 288
                    self.expr4(0) 
                self.state = 293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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

        def expr5(self):
            return self.getTypedRuleContext(HLangParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(HLangParser.Expr4Context,0)


        def LT(self):
            return self.getToken(HLangParser.LT, 0)

        def LTE(self):
            return self.getToken(HLangParser.LTE, 0)

        def GT(self):
            return self.getToken(HLangParser.GT, 0)

        def GTE(self):
            return self.getToken(HLangParser.GTE, 0)

        def getRuleIndex(self):
            return HLangParser.RULE_expr4



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HLangParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 295
            self.expr5(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 302
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HLangParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 297
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 298
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2013265920) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 299
                    self.expr5(0) 
                self.state = 304
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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

        def expr6(self):
            return self.getTypedRuleContext(HLangParser.Expr6Context,0)


        def expr5(self):
            return self.getTypedRuleContext(HLangParser.Expr5Context,0)


        def ADD(self):
            return self.getToken(HLangParser.ADD, 0)

        def SUB(self):
            return self.getToken(HLangParser.SUB, 0)

        def getRuleIndex(self):
            return HLangParser.RULE_expr5



    def expr5(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HLangParser.Expr5Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_expr5, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.expr6(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 313
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HLangParser.Expr5Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr5)
                    self.state = 308
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 309
                    _la = self._input.LA(1)
                    if not(_la==20 or _la==21):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 310
                    self.expr6(0) 
                self.state = 315
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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

        def expr7(self):
            return self.getTypedRuleContext(HLangParser.Expr7Context,0)


        def expr6(self):
            return self.getTypedRuleContext(HLangParser.Expr6Context,0)


        def MUL(self):
            return self.getToken(HLangParser.MUL, 0)

        def DIV(self):
            return self.getToken(HLangParser.DIV, 0)

        def MOD(self):
            return self.getToken(HLangParser.MOD, 0)

        def getRuleIndex(self):
            return HLangParser.RULE_expr6



    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HLangParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_expr6, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.expr7(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 324
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HLangParser.Expr6Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                    self.state = 319
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 320
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 29360128) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 321
                    self.expr7(0) 
                self.state = 326
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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

        def expr8(self):
            return self.getTypedRuleContext(HLangParser.Expr8Context,0)


        def expr7(self):
            return self.getTypedRuleContext(HLangParser.Expr7Context,0)


        def PIPELINE(self):
            return self.getToken(HLangParser.PIPELINE, 0)

        def getRuleIndex(self):
            return HLangParser.RULE_expr7



    def expr7(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HLangParser.Expr7Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expr7, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.expr8()
            self._ctx.stop = self._input.LT(-1)
            self.state = 335
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = HLangParser.Expr7Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr7)
                    self.state = 330
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 331
                    self.match(HLangParser.PIPELINE)
                    self.state = 332
                    self.expr8() 
                self.state = 337
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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

        def expr8(self):
            return self.getTypedRuleContext(HLangParser.Expr8Context,0)


        def NOT(self):
            return self.getToken(HLangParser.NOT, 0)

        def SUB(self):
            return self.getToken(HLangParser.SUB, 0)

        def ADD(self):
            return self.getToken(HLangParser.ADD, 0)

        def expr9(self):
            return self.getTypedRuleContext(HLangParser.Expr9Context,0)


        def getRuleIndex(self):
            return HLangParser.RULE_expr8




    def expr8(self):

        localctx = HLangParser.Expr8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expr8)
        self._la = 0 # Token type
        try:
            self.state = 341
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [20, 21, 33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 8593080320) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 339
                self.expr8()
                pass
            elif token in [6, 7, 12, 16, 17, 38, 42, 47, 48, 49, 50]:
                self.enterOuterAlt(localctx, 2)
                self.state = 340
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

        def getRuleIndex(self):
            return HLangParser.RULE_expr9




    def expr9(self):

        localctx = HLangParser.Expr9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_expr9)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self.primary_expr()
            self.state = 350
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 344
                    self.match(HLangParser.LSP)
                    self.state = 345
                    self.expr()
                    self.state = 346
                    self.match(HLangParser.RSP) 
                self.state = 352
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

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


        def type_conversion_call(self):
            return self.getTypedRuleContext(HLangParser.Type_conversion_callContext,0)


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
        self.enterRule(localctx, 72, self.RULE_primary_expr)
        try:
            self.state = 366
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.match(HLangParser.INT_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                self.match(HLangParser.FLOAT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 355
                self.match(HLangParser.STRING_LIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 356
                self.match(HLangParser.TRUE)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 357
                self.match(HLangParser.FALSE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 358
                self.array_lit()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 359
                self.type_conversion_call()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 360
                self.callexpr()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 361
                self.match(HLangParser.ID)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 362
                self.match(HLangParser.LP)
                self.state = 363
                self.expr()
                self.state = 364
                self.match(HLangParser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_conversion_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(HLangParser.INT, 0)

        def LP(self):
            return self.getToken(HLangParser.LP, 0)

        def exprlist(self):
            return self.getTypedRuleContext(HLangParser.ExprlistContext,0)


        def RP(self):
            return self.getToken(HLangParser.RP, 0)

        def FLOAT(self):
            return self.getToken(HLangParser.FLOAT, 0)

        def STR(self):
            return self.getToken(HLangParser.STR, 0)

        def getRuleIndex(self):
            return HLangParser.RULE_type_conversion_call




    def type_conversion_call(self):

        localctx = HLangParser.Type_conversion_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_type_conversion_call)
        try:
            self.state = 383
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.match(HLangParser.INT)
                self.state = 369
                self.match(HLangParser.LP)
                self.state = 370
                self.exprlist()
                self.state = 371
                self.match(HLangParser.RP)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 373
                self.match(HLangParser.FLOAT)
                self.state = 374
                self.match(HLangParser.LP)
                self.state = 375
                self.exprlist()
                self.state = 376
                self.match(HLangParser.RP)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 378
                self.match(HLangParser.STR)
                self.state = 379
                self.match(HLangParser.LP)
                self.state = 380
                self.exprlist()
                self.state = 381
                self.match(HLangParser.RP)
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


    class CallexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(HLangParser.ID, 0)

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
        self.enterRule(localctx, 76, self.RULE_callexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            self.match(HLangParser.ID)
            self.state = 386
            self.match(HLangParser.LP)
            self.state = 387
            self.exprlist()
            self.state = 388
            self.match(HLangParser.RP)
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
        self.enterRule(localctx, 78, self.RULE_array_lit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.match(HLangParser.LSP)
            self.state = 391
            self.exprlist()
            self.state = 392
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
        self.enterRule(localctx, 80, self.RULE_exprlist)
        self._la = 0 # Token type
        try:
            self.state = 403
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6, 7, 12, 16, 17, 20, 21, 33, 38, 42, 47, 48, 49, 50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.expr()
                self.state = 399
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==44:
                    self.state = 395
                    self.match(HLangParser.COMMA)
                    self.state = 396
                    self.expr()
                    self.state = 401
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [39, 43]:
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
        self._predicates[27] = self.expr1_sempred
        self._predicates[28] = self.expr2_sempred
        self._predicates[29] = self.expr3_sempred
        self._predicates[30] = self.expr4_sempred
        self._predicates[31] = self.expr5_sempred
        self._predicates[32] = self.expr6_sempred
        self._predicates[33] = self.expr7_sempred
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
         




