#complexidade: O(n)

class No:
    def __init__(self, valor=0, prox=None):
        self.valor = valor
        self.prox = prox


def contem_elemento_repetido(p):
    vistos = set()
    atual = p

    while atual:
        if atual.valor in vistos:
            return True
        vistos.add(atual.valor)
        atual = atual.prox

    return False

p1 = No(2, No(9, No(7, No(4, No(1)))))
resultado1 = "Sim" if contem_elemento_repetido(p1) else "Não"
print("Resultado para a lista da imagem:", resultado1)  


p2 = No(2, No(9, No(7, No(2, No(1)))))
resultado2 = "Sim" if contem_elemento_repetido(p2) else "Não"
print("Resultado para lista com repetição:", resultado2) 