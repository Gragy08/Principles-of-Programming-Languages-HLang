grammar HLang;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:
        result = super().emit()
        if self.text.endswith('\r\n'):
            raise UncloseString(self.text[1:-2])
        elif self.text.endswith('\n') or self.text.endswith('\r'):
            raise UncloseString(self.text[1:-1])
        else:
            raise UncloseString(self.text[1:])
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit()
        raise IllegalEscape(result.text[1:])
    elif tk == self.ERROR_CHAR:
        result = super().emit()
        raise ErrorToken(result.text)
    else:
        return super().emit()
}

options {
    language=Python3;
}

// ------------------ Parser ------------------

program: constdecl* funcdecl* EOF;

constdecl: CONST ID (COLON var_type)? ASSIGN expr SEMICOLON;
vardecl: LET ID (COLON var_type)? ASSIGN expr SEMICOLON;
funcdecl: FUNC ID paramdecl ARROW ret_type body;

var_type: non_void_type;
ret_type: non_void_type | VOID;
non_void_type: INT | FLOAT | BOOL | STRING | array_type;
array_type: LSP non_void_type SEMICOLON INT_LIT RSP;

idlist: ID idlist_tail;
idlist_tail: COMMA ID idlist_tail | ;

paramdecl: LP paramlist? RP;
paramlist: param paramlist_tail;
paramlist_tail: COMMA param paramlist_tail | ;
param: ID COLON var_type;

body: LCP stmt* RCP;

stmt
    : vardecl
    | assignment
    | callstmt
    | returnstmt
    | breakstmt
    | continuestmt
    | if_stmt
    | while_stmt
    | for_stmt
    | exprstmt
    | blockstmt
    ;

breakstmt: BREAK SEMICOLON;
continuestmt: CONTINUE SEMICOLON;
blockstmt: LCP stmt* RCP;
for_stmt: FOR LP ID IN expr RP body;
while_stmt: WHILE LP expr RP body;
if_stmt: IF LP expr RP body (ELSE else_stmt)?;
else_stmt: if_stmt | body;

assignment: lhs ASSIGN expr SEMICOLON;
lhs: ID lhs_tail;
lhs_tail: LSP expr RSP lhs_tail | ;

callstmt: callexpr SEMICOLON;
returnstmt: RETURN expr? SEMICOLON;
exprstmt: expr SEMICOLON;

// ------------------ Expressions ------------------
// expr: expr1;
// expr1: expr1 OR expr2 | expr2;
// expr2: expr2 AND expr3 | expr3;
// expr3: expr3 (EQUAL | UNEQUAL) expr4 | expr4;
// expr4: expr4 (LT | LTE | GT | GTE) expr5 | expr5;
// expr5: expr5 (ADD | SUB) expr6 | expr6;
// expr6: expr6 (MUL | DIV | MOD) expr7 | expr7;
// expr7: expr7 PIPELINE expr8 | expr8;
// expr8: (NOT | SUB | ADD) expr8 | expr9;
// expr9: primary_expr expr9_tail;
// expr9_tail: LSP expr RSP expr9_tail | ;

expr: expr1;
expr1: expr2;
expr2: expr2 PIPELINE expr3 | expr3;
expr3: expr3 OR expr4 | expr4;
expr4: expr4 AND expr5 | expr5;
expr5: expr5 (EQUAL | UNEQUAL) expr6 | expr6;
expr6: expr6 (LT | LTE | GT | GTE) expr7 | expr7;
expr7: expr7 (ADD | SUB) expr8 | expr8;
expr8: expr8 (MUL | DIV | MOD) expr9 | expr9;
expr9: (NOT | SUB | ADD) expr9 | primary_expr expr9_tail;
expr9_tail: LSP expr RSP expr9_tail | ;

primary_expr
    : INT_LIT
    | FLOAT_LIT
    | STRING_LIT
    | TRUE
    | FALSE
    | array_lit
    | type_conversion_call
    | callexpr
    | ID
    | LP expr RP
    ;

type_conversion_call
    : INT LP exprlist_opt RP
    | FLOAT LP exprlist_opt RP
    | STR LP exprlist_opt RP
    ;

callexpr: ID LP exprlist_opt RP ;
array_lit: LSP exprlist_opt RSP ;
exprlist_opt: exprlist | ;
exprlist: expr exprlist_tail ;
exprlist_tail: COMMA expr exprlist_tail | ;

// ------------------ Lexer ------------------

// Keywords
BOOL: 'bool';
BREAK: 'break';
CONST: 'const';
CONTINUE: 'continue';
ELSE: 'else';
FALSE: 'false';
FLOAT: 'float';
FOR: 'for';
FUNC: 'func';
IF: 'if';
IN: 'in';
INT: 'int';
LET: 'let';
RETURN: 'return';
STRING: 'string';
STR: 'str';
TRUE: 'true';
VOID: 'void';
WHILE: 'while';

// Operators
ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
MOD: '%';
EQUAL: '==';
UNEQUAL: '!=';
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';
AND: '&&';
OR: '||';
NOT: '!';
ASSIGN: '=';
COLON: ':';
ARROW: '->';
PIPELINE: '>>';

// Separators
LP: '(';
RP: ')';
LCP: '{';
RCP: '}';
LSP: '[';
RSP: ']';
COMMA: ',';
SEMICOLON: ';';
DOT: '.';

// Identifiers
ID: [a-zA-Z_][a-zA-Z0-9_]*;

// Literals
INT_LIT: [0-9]+;
FLOAT_LIT: [0-9]+ '.' [0-9]* ([Ee] [+-]? [0-9]+)?;
STRING_LIT: '"' STRING_CHAR* '"' {self.text = self.text[1:-1]};
fragment STRING_CHAR: ~[\n\r"\\] | ESC_SEQ;
fragment ESC_SEQ: '\\' [ntr"\\];

// Whitespace and Comments
WS: [ \t]+ -> skip;
NEWLINE: ('\r'? '\n' | '\r') -> skip;
COMMENT_LINE: '//' ~[\n\r]* -> skip;
COMMENT: '/*' (COMMENT | ~[*] | '*' ~[/])* '*/' -> skip;

// Error Tokens
UNCLOSE_STRING
    : '"' STRING_CHAR* ('\r\n' | '\n' | '\r' | EOF)
    ;

ILLEGAL_ESCAPE
    : '"' (STRING_CHAR | '\\' ~[ntr"\\])* '\\' ~[ntr"\\]
    ;

ERROR_CHAR: . ;