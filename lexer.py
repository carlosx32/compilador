import ply.lex as lex

tokens = [ 'VARIABLE','NUMERO','SUMAR','RESTAR','MULTIPLICAR','DIVIDIR', 'IGUAL','POTENCIA','COMPARACION','NEGACION']

t_ignore = ' \t'
t_SUMAR = r'\+'
t_RESTAR = r'-'
t_MULTIPLICAR = r'\*'
t_DIVIDIR = r'/'
t_IGUAL = r'='
t_VARIABLE = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_POTENCIA = r'\^'
t_COMPARACION = r'=='
t_NEGACION= r'!='

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
postfija="postfija.txt"
listaExpresiones = [x.strip('\n') for x in open(postfija, "r").readlines()]


lex.lex() # Build the lexer
for x in listaExpresiones:
    lex.input(x)
    while True:
        tok = lex.token()
        if not tok: break
        print str(tok.value) + " - " + str(tok.type)
