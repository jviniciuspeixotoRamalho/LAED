#Complexidade: O(n)

class No:
    def __init__(self, valor=0, prox=None, ant=None):
        self.valor = valor
        self.prox = prox
        self.ant = ant


def trocar_nos(cabeca, no1, no2):
  
    ant_no1 = no1.ant
    prox_no2 = no2.prox

    if ant_no1:
        ant_no1.prox = no2
    else:
        cabeca = no2

    no2.ant = ant_no1
    no2.prox = no1

    no1.ant = no2
    no1.prox = prox_no2

    if prox_no2:
        prox_no2.ant = no1

    return cabeca

def varredura(p):
    if not p or not p.prox:
        return p

    atual = p
    while atual and atual.prox:
        proximo = atual.prox
        if atual.valor > proximo.valor:
            p = trocar_nos(p, atual, proximo)
        else:
            atual = atual.prox

    return p

n1, n2, n3, n4, n5 = No(9), No(3), No(8), No(5), No(1)
n1.prox, n2.ant, n2.prox, n3.ant = n2, n1, n3, n2
n3.prox, n4.ant, n4.prox, n5.ant = n4, n3, n5, n4

p = varredura(n1)

atual = p
elementos = []
while atual:
    elementos.append(str(atual.valor))
    atual = atual.prox
print(" <-> ".join(elementos))  