class No:
    def __init__(self, valor=0, prox=None):
        self.valor = valor
        self.prox = prox


def intersecao_listas(p1, p2):
    elementos_p2 = set()
    atual2 = p2
    while atual2:
        elementos_p2.add(atual2.valor)
        atual2 = atual2.prox

    cabeca_sentinela = No(0)
    cauda = cabeca_sentinela
    adicionados = set()

    atual1 = p1
    while atual1:
        if atual1.valor in elementos_p2 and atual1.valor not in adicionados:
            cauda.prox = No(atual1.valor)
            cauda = cauda.prox
            adicionados.add(atual1.valor)
        atual1 = atual1.prox

    return cabeca_sentinela.prox

p1 = No(3, No(9, No(2, No(6, No(4)))))
p2 = No(4, No(5, No(2, No(9, No(3)))))

p = intersecao_listas(p1, p2)

atual = p
elementos = []
while atual:
    elementos.append(str(atual.valor))
    atual = atual.prox
print(" -> ".join(elementos))  