#Complexidade: O(n)

class No:
    def __init__(self, valor=0, prox=None, ant=None):
        self.valor = valor
        self.prox = prox
        self.ant = ant


def encontrar_elemento_central(p):
    if not p:
        return None

    lento = p
    rapido = p

    while rapido.prox and rapido.prox.prox:
        lento = lento.prox
        rapido = rapido.prox.prox

    return lento.valor

n1 = No(3)
n2 = No(9)
n3 = No(5)
n4 = No(2)
n5 = No(8)

n1.prox = n2
n2.ant = n1
n2.prox = n3
n3.ant = n2
n3.prox = n4
n4.ant = n3
n4.prox = n5
n5.ant = n4

p = n1
central = encontrar_elemento_central(p)
print("Elemento central:", central)