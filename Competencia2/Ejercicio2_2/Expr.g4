grammar Expr;

root : expr EOF;

expr : NUM MENOS NUM | NUM ;
NUM : [0-9]+;
ID : [a-zA-Z]+ ;
MENOS: '-';
MAS: '+';
IGUAL: '=' ;
WS: [ \n]+ -> skip ;