from lark import Lark

def sintax_analisis(expression):
    grammar = r"""
        start: expr
        ?expr: IF expr COMP expr THEN "{" expr "}"  ELSE THEN "{" expr "}"  
            |IF expr COMP expr THEN "{" expr "}" 
            |WHILE expr COMP expr THEN "{" expr "}" 
            | STRING
            | NUMBER
            | BOOL
            | ID
            |ID ASSING expr 
            |expr ASSING expr 
            |expr (OP)* expr
            |expr (COMP)* expr
            |ID (COMP)* expr
            |"(" expr ")"
        IF: "if"
        OP: "+" | "-" | "*" | "/"|"^"
        ASSING: "="
        THEN: ":"
        COMP: "==" | "!=" | "<" | ">" | "<=" | ">="
        ELSE: "else"
        STRING: /"[^"]*"/
        ID: /[a-zA-Z_]\w*/
        WHILE: "while"
        NUMBER: /\d+(\.\d+)?/ 
        BOOL: "$true" | "$false"
        %ignore " " | "\n"
    """

    parser = Lark(grammar)

    #expression = "if x == 5: a else y"
    tree = parser.parse(expression)

    return (tree,tree.pretty())