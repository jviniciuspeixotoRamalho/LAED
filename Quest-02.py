#Complexidade: O(n)

class No:
    def __init__(self, valor=0, prox=None, ant=None):
        self.valor = valor
        self.prox = prox
        self.ant = ant


def atualizar_elemento(p, x, y):
    if not p:
        return None

    atual = p
    while atual and atual.valor != x:
        atual = atual.prox

    if not atual:
        return p

    atual.valor = y

    if atual.ant:
        atual.ant.prox = atual.prox
    else:
        p = atual.prox  

    if atual.prox:
        atual.prox.ant = atual.ant

    atual.ant = None
    atual.prox = None

    if not p:
        return atual

    if y < p.valor:
        atual.prox = p
        p.ant = atual
        return atual

    temp = p
    while temp.prox and temp.prox.valor < y:
        temp = temp.prox

    atual.prox = temp.prox
    atual.ant = temp
    if temp.prox:
        temp.prox.ant = atual
    temp.prox = atual

    return p

n1, n2, n3, n4, n5 = No(3), No(5), No(9), No(10), No(15)
n1.prox, n2.ant, n2.prox, n3.ant = n2, n1, n3, n2
n3.prox, n4.ant, n4.prox, n5.ant = n4, n3, n5, n4

p = atualizar_elemento(n1, 9, 12)


atual = p
elementos = []
while atual:
    elementos.append(str(atual.valor))
    atual = atual.prox
print(" <-> ".join(elementos))  