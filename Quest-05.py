class No:
    def __init__(self, valor=0, pos=0, prox=None, ant=None):
        self.valor = valor
        self.pos = pos
        self.prox = prox
        self.ant = ant


def criar_vetor_esparso(vetor):
    cabeca_sentinela = No()
    cauda = cabeca_sentinela

    for indice, valor in enumerate(vetor, start=1):
        if valor != 0:
            novo_no = No(valor=valor, pos=indice)
            cauda.prox = novo_no
            novo_no.ant = cauda
            cauda = novo_no

    cabeca = cabeca_sentinela.prox
    if cabeca:
        cabeca.ant = None

    return cabeca

V = [0, 3, 0, 0, 0, 5, 0, 2, 0, 0, 8, 0, 0, 7, 0]
p = criar_vetor_esparso(V)

atual = p
elementos = []
while atual:
    elementos.append(f"[{atual.valor} | {atual.pos}]")
    atual = atual.prox
print(" <-> ".join(elementos)) 