#Tempo de execução do algoritmo: O(n)

class No:
    def __init__(self, valor=0, prox=None):
        self.valor = valor
        self.prox = prox


def particionar_lista(p, k):
    cabeca_menor = No(0)
    cabeca_maior = No(0)

    cauda_menor = cabeca_menor
    cauda_maior = cabeca_maior

    atual = p
    while atual:
        proximo_no = atual.prox


        if atual.valor <= k:
            cauda_menor.prox = atual
            cauda_menor = atual
        else:
            cauda_maior.prox = atual
            cauda_maior = atual

        atual = proximo_no


    cauda_menor.prox = cabeca_maior.prox
    cauda_maior.prox = None

    return cabeca_menor.prox



p = No(9, No(2, No(5, No(6, No(1)))))
k = 5
p = particionar_lista(p, k)

# Exibição do resultado
atual = p
elementos = []
while atual:
    elementos.append(str(atual.valor))
    atual = atual.prox
print(" -> ".join(elementos))  