class No:
    def __init__(self, valor=0, prox=None, ant=None):
        self.valor = valor
        self.prox = prox
        self.ant = ant


def transformar_em_lista_de_listas(p, k):
    if not p or k <= 0:
        return []

    n = 0
    atual = p
    while atual:
        n += 1
        atual = atual.prox

    k = min(k, n)

    tam_base = n // k
    resto = n % k

    L = []
    atual = p

    for i in range(k):
        L.append(atual)
        tam_sublista = tam_base + (1 if i < resto else 0)

        for _ in range(tam_sublista - 1):
            if atual:
                atual = atual.prox

        if atual and atual.prox:
            proximo_inicio = atual.prox
            atual.prox = None
            proximo_inicio.ant = None
            atual = proximo_inicio

    return L

valores = [1, 3, 7, 10, 13, 18, 21, 27, 30, 35]
nos = [No(v) for v in valores]
for i in range(len(nos) - 1):
    nos[i].prox = nos[i + 1]
    nos[i + 1].ant = nos[i]

p = nos[0]
k = 4
L = transformar_em_lista_de_listas(p, k)


for idx, cabeca_sublista in enumerate(L):
    elementos = []
    atual = cabeca_sublista
    while atual:
        elementos.append(str(atual.valor))
        atual = atual.prox
    print(f"L[{idx}] -> " + " <-> ".join(elementos))