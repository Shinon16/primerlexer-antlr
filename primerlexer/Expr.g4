grammar Expr;

prog: stat+;

stat: expr NEWLINE
    ;

expr: expr op expr
    | INT
    ;

op: '+'
  | '-'
  | '*'
  | '/'
  ;

INT: [0-9]+;

WS: [ \t\r\n]+ -> skip;