grammar Expr;

root : expr EOF ;

expr : ID IGUAL NUM ;

NUM : [0-9]+;

ID : [a-zA-Z]+ ;

IGUAL: '=' ;

WS: [ \n]+ -> skip ;