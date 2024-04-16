from lark import Lark

grammar = r"""
    start: expr
    ?expr: IF expr "==" expr ELSE expr
         | FALSE
         | STRING
         | ID
         | WHILE
         | NUMBER
         | TRUE
         | FOR
         | IF
    IF: "if"
    ELSE: "else"
    FALSE: "false"
    STRING: /"[^"]*"/
    ID: /[a-zA-Z_]\w*/
    WHILE: "while"
    NUMBER: /\d+/
    TRUE: "true"
    FOR: "for"
    %ignore " "
"""

parser = Lark(grammar)

expression = "if x == 5 else y"
tree = parser.parse(expression)

print(tree)
