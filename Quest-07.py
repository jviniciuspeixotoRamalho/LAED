#Complexidade: O(n)

class No:
    def __init__(self, valor=0, prox=None):
        self.valor = valor
        self.prox = prox


def remover_copias(p, k):
    cabeca_sentinela = No(0, p)
    anterior = cabeca_sentinela
    atual = p

    while atual:
        if atual.valor == k:
            anterior.prox = atual.prox
        else:
            anterior = atual
        atual = atual.prox

    return cabeca_sentinela.prox

p = No(1, No(3, No(3, No(2, No(3, No(2))))))
k = 3
p = remover_copias(p, k)

# Exibição do resultado
atual = p
elementos = []
while atual:
    elementos.append(str(atual.valor))
    atual = atual.prox
print(" -> ".join(elementos))  