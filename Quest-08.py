class No:

  def __init__(self, valor=0, prox=None, ant=None):
    self.valor = valor
    self.prox = prox
    self.ant = ant


def encontrar_sublista(L, x):
  inicio, fim = 0, len(L) - 1
  idx = 0

  while inicio <= fim:
    meio = (inicio + fim) // 2
    if L[meio].valor <= x:
      idx = meio
      inicio = meio + 1
    else:
      fim = meio - 1

  return idx


def busca(L, x):
  if not L:
    return False

  idx = encontrar_sublista(L, x)
  atual = L[idx]

  while atual and atual.valor <= x:
    if atual.valor == x:
      return True
    atual = atual.prox

  return False


def insercao(L, x):
  novo_no = No(x)

  if not L:
    L.append(novo_no)
    return L

  if x < L[0].valor:
    novo_no.prox = L[0]
    L[0].ant = novo_no
    L[0] = novo_no
    return L

  idx = encontrar_sublista(L, x)
  atual = L[idx]
  anterior = None

  while atual and atual.valor < x:
    anterior = atual
    atual = atual.prox

  if anterior:
    novo_no.prox = atual
    novo_no.ant = anterior
    anterior.prox = novo_no
    if atual:
      atual.ant = novo_no
  else:
    novo_no.prox = L[idx]
    L[idx].ant = novo_no
    L[idx] = novo_no
  return L

def remocao(L, x):
  if not L:
    return L

  idx = encontrar_sublista(L, x)
  atual = L[idx]

  while atual and atual.valor < x:
    atual = atual.prox

  if atual and atual.valor == x:
    if atual.ant:
      atual.ant.prox = atual.prox
    else:
      L[idx] = atual.prox

    if atual.prox:
      atual.prox.ant = atual.ant

    if L[idx] is None:
      L.pop(idx)
  return L

n1, n2 = No(2), No(9)
n1.prox, n2.ant = n2, n1

n3, n4 = No(15), No(19)
n3.prox, n4.ant = n4, n3

n5, n6 = No(31), No(49)
n5.prox, n6.ant = n6, n5

L = [n1, n3, n5]


print("Busca por 19:", busca(L, 19))  
print("Busca por 20:", busca(L, 20))  

L = insercao(L, 17) 
L = remocao(L, 9)  

for i, sublista in enumerate(L):
  elementos = []
  atual = sublista
  while atual:
    elementos.append(str(atual.valor))
    atual = atual.prox
  print(f"L[{i}] -> " + " <-> ".join(elementos))