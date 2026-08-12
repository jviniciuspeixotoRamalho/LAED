class No:
    def __init__(self, valor=0, pos=0, prox=None, ant=None):
        self.valor = valor
        self.pos = pos
        self.prox = prox
        self.ant = ant


def busca_por_indice(p, k):
    atual = p
    while atual and atual.pos <= k:
        if atual.pos == k:
            return atual.valor
        atual = atual.prox
    return 0


def busca_por_valor(p, x):
    atual = p
    while atual:
        if atual.valor == x:
            return atual.pos
        atual = atual.prox
    return -1


def atualizacao(p, x, k):
    atual = p
    anterior = None

    while atual and atual.pos < k:
        anterior = atual
        atual = atual.prox

    if atual and atual.pos == k:
        if x != 0:
            atual.valor = x
        else:
            if atual.ant:
                atual.ant.prox = atual.prox
            else:
                p = atual.prox 

            if atual.prox:
                atual.prox.ant = atual.ant
        return p

    if x != 0:
        novo_no = No(valor=x, pos=k)

        if not p:
            return novo_no

        if not atual:
            anterior.prox = novo_no
            novo_no.ant = anterior
        elif atual == p:
            novo_no.prox = p
            p.ant = novo_no
            p = novo_no
        else:
            novo_no.prox = atual
            novo_no.ant = atual.ant
            atual.ant.prox = novo_no
            atual.ant = novo_no

    return p

n1, n2, n3, n4, n5 = No(4, 3), No(5, 7), No(10, 9), No(1, 12), No(9, 17)
n1.prox, n2.ant, n2.prox, n3.ant = n2, n1, n3, n2
n3.prox, n4.ant, n4.prox, n5.ant = n4, n3, n5, n4
p = n1

print("Busca por índice 7:", busca_por_indice(p, 7))  
print("Busca por índice 8:", busca_por_indice(p, 8))  
print("Busca por valor 10:", busca_por_valor(p, 10))  
print("Busca por valor 99:", busca_por_valor(p, 99))  


p = atualizacao(p, 0, 7)
p = atualizacao(p, 6, 8)

atual = p
elementos = []
while atual:
    elementos.append(f"[{atual.valor}|{atual.pos}]")
    atual = atual.prox
print(" <-> ".join(elementos))  