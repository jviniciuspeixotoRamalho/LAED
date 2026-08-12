class No:

  def __init__(self, valor):
    self.valor = valor
    self.prox = None


class Fila:

  def __init__(self):
    self.inicio = None
    self.fim = None

  def enqueue(self, valor):
    novo = No(valor)
    if not self.fim:
      self.inicio = self.fim = novo
    else:
      self.fim.prox = novo
      self.fim = novo

  def dequeue(self):
    if not self.inicio:
      return None
    val = self.inicio.valor
    self.inicio = self.inicio.prox
    if not self.inicio:
      self.fim = None
    return val

  def para_lista(self):
    atual = self.inicio
    res = []
    while atual:
      res.append(atual.valor)
      atual = atual.prox
    return res

f = Fila()
for v in [1, 2, 3, 4]:
  f.enqueue(v)

pilha = []
while f.inicio:
  pilha.append(f.dequeue())

while pilha:
  f.enqueue(pilha.pop())

print("Resultado com pilha:", f.para_lista()) 

def inverter_in_place(fila):
  anterior = None
  atual = fila.inicio
  fila.fim = fila.inicio 

  while atual:
    proximo = atual.prox
    atual.prox = anterior
    anterior = atual
    atual = proximo

  fila.inicio = anterior

f2 = Fila()
for v in [1, 2, 3, 4]:
  f2.enqueue(v)

inverter_in_place(f2)
print("Resultado in-place:", f2.para_lista())