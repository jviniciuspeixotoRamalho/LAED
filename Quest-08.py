#Complexidade: O(n)

class No:
    def __init__(self, valor=0, prox=None):
        self.valor = valor
        self.prox = prox


def elemento_mais_frequente(p):
    if not p:
        return None, 0

    frequencias = {}
    mais_frequente = None
    max_ocorrencias = 0

    atual = p
    while atual:
        valor_atual = atual.valor
        frequencias[valor_atual] = frequencias.get(valor_atual, 0) + 1

        if frequencias[valor_atual] > max_ocorrencias:
            max_ocorrencias = frequencias[valor_atual]
            mais_frequente = valor_atual

        atual = atual.prox

    return mais_frequente, max_ocorrencias



p = No(8, No(3, No(8, No(5, No(8, No(3))))))
elemento, contagem = elemento_mais_frequente(p)

print(f"{elemento} é o elemento que aparece mais vezes, com {contagem} ocorrências")