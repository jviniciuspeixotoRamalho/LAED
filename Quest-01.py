#Algoritmo com tempo de execução O(n)

class No:
    def __init__(self, valor=0, prox=None):
        self.valor = valor
        self.prox = prox


def mover_maior_para_o_fim(cabeca):
    if not cabeca or not cabeca.prox:
        return cabeca

    maior_no = cabeca
    maior_ant = None
    atual = cabeca
    ant = None
    cauda = cabeca

    while atual:
        if atual.valor > maior_no.valor:
            maior_no = atual
            maior_ant = ant
        cauda = atual
        ant = atual
        atual = atual.prox

    # Caso o maior elemento já esteja na última posição
    if maior_no == cauda:
        return cabeca

    # Desconecta o maior nó de sua posição original
    if maior_ant is None:
        cabeca = cabeca.prox
    else:
        maior_ant.prox = maior_no.prox

    # Conecta o maior nó no final da lista
    cauda.prox = maior_no
    maior_no.prox = None

    return cabeca


# Teste: 5 -> 8 -> 13 -> 2 -> 10
p = No(5, No(8, No(13, No(2, No(10)))))
p = mover_maior_para_o_fim(p)

# Exibição do resultado
atual = p
elementos = []
while atual:
    elementos.append(str(atual.valor))
    atual = atual.prox
print(" -> ".join(elementos))  