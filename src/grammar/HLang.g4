grammar HLang;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:
        result = super().emit();
        if len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r':
            raise UncloseString(result.text[1:-2])
        elif self.text[-1] == '\n' or self.text[-1] == '\r':
            raise UncloseString(result.text[1:-1])
        else:
            raise UncloseString(result.text[1:])
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text[1:]) 
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text)
    else:
        return super().emit();
}

options {
    language=Python3;
}

//------------------Parser------------------

program: decl* EOF;

decl: constdecl | funcdecl;

constdecl: CONST ID (COLON var_type)? ASSIGN expr SEMICOLON;

vardecl: LET ID (COLON var_type)? ASSIGN expr SEMICOLON;

funcdecl: FUNC ID paramdecl ARROW ret_type body;

var_type: non_void_type;
ret_type: non_void_type | VOID;

non_void_type: INT | FLOAT | BOOL | STRING | array_type;

array_type: LSP non_void_type SEMICOLON INT_LIT RSP;

idlist: ID (COMMA ID)*;

paramdecl: LP paramlist? RP;
paramlist: param (COMMA param)*;
param: ID COLON var_type;

body: LCP stmt* RCP;

stmt
    : vardecl
    | assignment
    | callstmt
    | returnstmt
    | if_stmt
    | while_stmt
    | for_stmt
    | exprstmt
    ;

for_stmt: FOR LP ID IN expr RP body;

while_stmt: WHILE LP expr RP body;

if_stmt
    : IF LP expr RP body (ELSE body)?
    ;

assignment: postfix_expr ASSIGN expr SEMICOLON;

callstmt: callexpr SEMICOLON;

returnstmt: RETURN expr? SEMICOLON;

exprstmt: expr SEMICOLON;

exprlist: expr (COMMA expr)*;

array_lit: LSP exprlist? RSP;

// Expressions
expr: expr1 (PIPELINE expr1)*;

expr1: expr2 (OR expr2)*;

expr2: expr3 (AND expr3)*;

expr3: expr4 ((EQUAL | UNEQUAL | LT | LTE | GT | GTE) expr4)*;

expr4: expr5 ((ADD | SUB) expr5)*;

expr5: expr6 ((MUL | DIV | MOD) expr6)*;

expr6: unary_expr | postfix_expr;

unary_expr: (ADD | SUB | NOT) expr6;

postfix_expr: primary_expr (LSP expr RSP)*;

primary_expr
    : INT_LIT
    | FLOAT_LIT
    | STRING_LIT
    | TRUE
    | FALSE
    | ID
    | callexpr
    | subexpr
    | array_lit
    ;

callexpr: (ID | INT | FLOAT | BOOL | STRING) LP exprlist? RP;

subexpr: LP expr RP;

//------------------Lexer------------------

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
    {
        if self.text.endswith('\r\n'):
            raise UncloseString(self.text[1:-2] + '\r\n')
        elif self.text.endswith('\n'):
            raise UncloseString(self.text[1:-1] + '\n')
        elif self.text.endswith('\r'):
            raise UncloseString(self.text[1:-1] + '\r')
        else:
            raise UncloseString(self.text[1:])
    }
    ;

ILLEGAL_ESCAPE
    : '"' (STRING_CHAR | '\\' ~[ntr"\\])* '\\' ~[ntr"\\]
    {
        raise IllegalEscape(self.text[1:])
    }
    ;

ERROR_CHAR: . {raise ErrorToken(self.text)};