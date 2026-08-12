#Tempo de execução do algoritmo: O(n)

class No:
    def __init__(self, valor=0, prox=None):
        self.valor = valor
        self.prox = prox


def separar_impares_pares(p):
    # Nós sentinelas (falsos cabeças) para facilitar a montagem das listas
    cabeca_impar = No(0)
    cabeca_par = No(0)

    cauda_impar = cabeca_impar
    cauda_par = cabeca_par

    atual = p
    while atual:
        proximo_no = atual.prox

        # Verifica se o valor é ímpar
        if atual.valor % 2 != 0:
            cauda_impar.prox = atual
            cauda_impar = atual
        else:
            cauda_par.prox = atual
            cauda_par = atual

        atual = proximo_no

    # Garante o término de ambas as listas
    cauda_impar.prox = None
    cauda_par.prox = None

    p1 = cabeca_impar.prox  # Ponteiro para a lista de ímpares
    p2 = cabeca_par.prox  # Ponteiro para a lista de pares

    return p1, p2


# Teste: 2 -> 8 -> 5 -> 10 -> 7
p = No(2, No(8, No(5, No(10, No(7)))))
p1, p2 = separar_impares_pares(p)


# Exibição dos resultados
def exibir_lista(no_inicial):
    elementos = []
    atual = no_inicial
    while atual:
        elementos.append(str(atual.valor))
        atual = atual.prox
    return " -> ".join(elementos)


print("p1 (ímpares):", exibir_lista(p1))  
print("p2 (pares):", exibir_lista(p2))  