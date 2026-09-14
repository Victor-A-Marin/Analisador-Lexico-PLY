import ply.yacc as yacc

import lexico
from lexico import tokens
import tabela_simbolos

def p_programa(p):
    """
    programa : lista_declaracoes
    """

def p_lista_declaracoes(p):
    """
    lista_declaracoes : lista_declaracoes declaracao
                      | declaracao
    """

def p_declaracao(p):
    """
    declaracao : TIPO lista_ids PV
    """
    tipo = p[1]
    for nome, linha in p[2]:
        tabela_simbolos.adiciona_simbolo(nome, tipo, linha)

def p_lista_ids(p):
    """
    lista_ids : ID
              | lista_ids VIRG ID
    """
    if len(p) == 2:
        p[0] = [(p[1], p.lineno(1))]
    else:
        p[0] = p[1] + [(p[3], p.lineno(3))]

def p_error(p):
    if p:
        print(
            f"ERRO SINTATICO: token inesperado "
            f"'{p.value}' na linha {p.lineno}"
        )
        tabela_simbolos.adiciona_simbolo(
            p.value, "erro", p.lineno, categoria="erro"
        )
    else:
        print("ERRO SINTATICO: fim inesperado do programa")

parser = yacc.yacc(write_tables=False, debug=False)

def analisa(programa):
    tabela_simbolos.tabela_simbolos.clear()

    lexico.lexer.lineno = 1
    lexico.erros_lexicos.clear()
    lexico.imprimir_erros = False
    try:
        parser.parse(programa, lexer=lexico.lexer)
    finally:
        lexico.imprimir_erros = True      # restaura para a próxima chamada

    linhas_com_erro = {linha for linha, _ in lexico.erros_lexicos}
    for simbolo in tabela_simbolos.tabela_simbolos:
        if simbolo["linha"] in linhas_com_erro:
            simbolo["categoria"] = "erro"
            simbolo["tipo"] = "erro"

    tabela_simbolos.imprime_tabela()