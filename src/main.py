import os

import lexico
import parser
import tabela_simbolos

PASTA_TESTES = "testes"

ARQUIVOS_VALIDOS = [
    "valido1.c",
    "valido2.c",
    "valido3.c",
]

ARQUIVOS_INVALIDOS = [
    "invalido1.c",
    "invalido2.c",
    "invalido3.c",
]

def separador(titulo):
    print("\n" + "=" * 60)
    print(titulo)
    print("=" * 60)

def processa_arquivo(caminho, esperado):
    with open(caminho, "r", encoding="utf-8") as f:
        programa = f.read()

    separador(f"ARQUIVO: {caminho}  (esperado: {esperado.upper()})")
    print("--- PROGRAMA ---")
    print(programa.rstrip())
    print()

    print("--- TOKENS ---")
    lexico.analisa(programa)

    print("--- PARSER + TABELA ---")
    parser.analisa(programa)

def main():
    separador("TESTES VALIDOS")
    for nome in ARQUIVOS_VALIDOS:
        caminho = os.path.join(PASTA_TESTES, nome)
        processa_arquivo(caminho, "valido")

    separador("TESTES INVALIDOS")
    for nome in ARQUIVOS_INVALIDOS:
        caminho = os.path.join(PASTA_TESTES, nome)
        processa_arquivo(caminho, "invalido")

if __name__ == "__main__":
    main()