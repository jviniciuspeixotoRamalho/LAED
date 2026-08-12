#Tempo de execução: O(n)

class No:
    def __init__(self, valor=0, prox=None):
        self.valor = valor
        self.prox = prox


def inverter_lista(p):
    anterior = None
    atual = p

    while atual:
        proximo = atual.prox  
        atual.prox = anterior  
        anterior = atual  
        atual = proximo  

    return anterior 


# Teste: 3 -> 2 -> 5 -> 9 -> 4
p = No(3, No(2, No(5, No(9, No(4)))))
p = inverter_lista(p)

# Exibição do resultado
atual = p
elementos = []
while atual:
    elementos.append(str(atual.valor))
    atual = atual.prox
print(" -> ".join(elementos))  