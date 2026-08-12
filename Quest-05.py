class No:
    def __init__(self, valor=0, prox=None):
        self.valor = valor
        self.prox = prox


def intercalar_listas(p1, p2):
    cabeca_sentinela = No(0)
    cauda = cabeca_sentinela

    atual1 = p1
    atual2 = p2


    while atual1 and atual2:
        if atual1.valor <= atual2.valor:
            cauda.prox = atual1
            atual1 = atual1.prox
        else:
            cauda.prox = atual2
            atual2 = atual2.prox
        cauda = cauda.prox

    
    if atual1:
        cauda.prox = atual1
    elif atual2:
        cauda.prox = atual2

    return cabeca_sentinela.prox


# Teste:
# p1: 3 -> 6 -> 7 -> 10 -> 13
# p2: 2 -> 4 -> 9 -> 11 -> 12
p1 = No(3, No(6, No(7, No(10, No(13)))))
p2 = No(2, No(4, No(9, No(11, No(12)))))

p = intercalar_listas(p1, p2)

# Exibição do resultado
atual = p
elementos = []
while atual:
    elementos.append(str(atual.valor))
    atual = atual.prox
print(" -> ".join(elementos))  