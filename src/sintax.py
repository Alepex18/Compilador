from lark import Lark

def sintax_analisis(expression):
    grammar = r"""
        start: expr
        ?expr: IF expr COMP expr THEN expr ELSE expr
            | FALSE
            | STRING
            | ID 
            | WHILE
            | NUMBER
            | TRUE
            | FOR
            | IF
            |ID ASSING expr 
            |expr (OP)* expr
            |expr (COMP)* expr
        IF: "if"
        OP: "+" | "-" | "*" | "/"
        ASSING: "="
        THEN: ":"
        COMP: "==" | "!=" | "<" | ">" | "<=" | ">="
        ELSE: "else"
        FALSE: "false"
        STRING: /"[^"]*"/
        ID: /[a-zA-Z_]\w*/
        WHILE: "while"
        NUMBER: /\d+(\.\d+)?/ 
        TRUE: "true"
        FOR: "for"
        %ignore " "
    """

    parser = Lark(grammar)

    #expression = "if x == 5: a else y"
    tree = parser.parse(expression)

    return (tree,tree.pretty())