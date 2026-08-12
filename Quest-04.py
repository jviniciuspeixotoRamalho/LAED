#Complexidade: O(n)

class No:
    def __init__(self, valor=0, prox=None, ant=None):
        self.valor = valor
        self.prox = prox
        self.ant = ant


def particionar_lista(p, k):
    if not p or not p.prox:
        return p

    q = p
    r = p
    while r.prox:
        r = r.prox

    while q != r:
        while q != r and q.valor <= k:
            q = q.prox

        while q != r and r.valor > k:
            r = r.ant

        if q != r:
            q.valor, r.valor = r.valor, q.valor

    return p

n1, n2, n3, n4, n5 = No(12), No(5), No(9), No(17), No(13)
n1.prox, n2.ant, n2.prox, n3.ant = n2, n1, n3, n2
n3.prox, n4.ant, n4.prox, n5.ant = n4, n3, n5, n4

p = particionar_lista(n1, 10)

# Exibição do resultado
atual = p
elementos = []
while atual:
    elementos.append(str(atual.valor))
    atual = atual.prox
print(" <-> ".join(elementos))