grammar Expr;

root : ID IGUAL NUM EOF ;

expr : ID IGUAL NUM | NUM ;

NUM : [0-9]+;

ID : [a-zA-Z]+ ;

IGUAL: '=' ;

WS: [ \n]+ -> skip ;