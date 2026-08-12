#Tempo de execução: O(n)

class No:
    def __init__(self, valor=0, prox=None):
        self.valor = valor
        self.prox = prox


def duplicar_impares(p):
    atual = p

    while atual:
       
        if atual.valor % 2 != 0:
            novo_no = No(atual.valor, atual.prox)
            atual.prox = novo_no
            atual = novo_no.prox
        else:
            atual = atual.prox

    return p


# Teste: 2 -> 7 -> 6 -> 3
p = No(2, No(7, No(6, No(3))))
p = duplicar_impares(p)

# Exibição do resultado
atual = p
elementos = []
while atual:
    elementos.append(str(atual.valor))
    atual = atual.prox
print(" -> ".join(elementos))  