grammar Expr;

root : expr EOF ;

expr : IF ID MAY NUM  ;
IF: 'if';

NUM : [0-9]+;

ID : [a-zA-Z]+ ;
MAY: '>';
IGUAL: '=' ;

WS: [ \n]+ -> skip ;