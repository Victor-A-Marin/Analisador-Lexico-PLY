import ply.lex as lex

erros_lexicos = []
imprimir_erros = True

tokens = (
    "TIPO",
    "ID",
    "VIRG",
    "PV",
)

def t_TIPO(t):
    r"(char|int|float)\b"
    return t

t_ID = r"[a-zA-Z_][a-zA-Z0-9_]*"
t_VIRG = r","
t_PV = r";"

t_ignore = " \t"

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

def t_error(t):
    if imprimir_erros:
        print(f"\n[linha {t.lexer.lineno}] ERRO LEXICO: '{t.value[0]}'")
    erros_lexicos.append((t.lexer.lineno, t.value[0]))
    t.lexer.skip(1)

lexer = lex.lex()

def analisa(programa):
    lexer.lineno = 1
    erros_lexicos.clear()
    imprimir_erros = True
    lexer.input(programa)
    for tok in lexer:
        print(f"{tok.type}({tok.value})", end=" ")
    print()