import ply.lex as lex

tokens = [  'VARIABLE','NUMERO','SUMAR','RESTAR',
            'MULTIPLICAR','DIVIDIR', 'IGUAL','POTENCIA',
            'ESIGUAL','NEGACION','CONDICIONSI','CICLOPARA',
            'MAYOR','MENOR','MAYORIGUAL','MENORIGUAL','PRENTESIS','CADENA_CARACTERES','DOSPUNTOS','COMENTARIO'
        ]
condicionLIST=['SI','SINO','ENTONCES']
paraList=['PARA','HASTA','SALTANDO','HACER']


t_ignore = ' \t'
t_SUMAR = r'\+'
t_RESTAR = r'-'
t_MULTIPLICAR = r'\*'
t_DIVIDIR = r'/'
t_IGUAL = r'='
#t_VARIABLE = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_POTENCIA = r'\^'
t_ESIGUAL = r'=='
t_NEGACION= r'!='
t_MAYOR = r'>'
t_MENOR = r'<'
t_MAYORIGUAL    = r'>='
t_MENORIGUAL    = r'<='
t_PRENTESIS	= '[\(][a-zA-Z]*[)]'
t_CADENA_CARACTERES= '["\'][a-zA-Z]*[\'"]'
t_DOSPUNTOS	= ':'

def t_COMENTARIO(t):
    r'\#.*'
    return t


def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    #r'[S][I] | [s][i]'
    for r in condicionLIST:
            if r.upper() == t.value.upper():
                t.type = 'CONDICIONSI'
                return t
    for r in paraList:
            if r.upper() == t.value.upper():
                t.type = 'CICLOPARA'
                return t
    return t


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
