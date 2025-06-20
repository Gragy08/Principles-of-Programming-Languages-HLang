grammar HLang;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}

program  : EOF ;

REAL_LITERAL
  : DIGIT+ '.' DIGIT+ ( [eE] [+-]? DIGIT+ )?
  | DIGIT+ [eE] [+-]? DIGIT+
  ;

ID : [a-df-z] [a-z0-9]* ; // loại trừ 'e' đầu để tránh nhầm lẫn với scientific notation

fragment DIGIT : [0-9] ;

STRING_LITERAL
  : '\'' ( '\'\'' | ~[\r\n'] )* '\''
  ;

WS : [ \t\r]+ -> skip ; // skip spaces, tabs 

ERROR_CHAR: .;
ILLEGAL_ESCAPE:.;
UNCLOSE_STRING:.;