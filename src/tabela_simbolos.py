tabela_simbolos = []

def adiciona_simbolo(nome, tipo, linha, categoria="variável"):
    tabela_simbolos.append({
        "nome": nome,
        "tipo": tipo,
        "linha": linha,
        "categoria": categoria
    })

def imprime_tabela():
    print("\nTABELA DE SIMBOLOS:")
    print("Nome\tTipo\tLinha\tCategoria")
    for simbolo in tabela_simbolos:
        print(
            f"{simbolo['nome']}\t"
            f"{simbolo['tipo']}\t"
            f"{simbolo['linha']}\t"
            f"{simbolo['categoria']}"
        )