class No:

  def __init__(self, valor, minimo, prox=None):
    self.valor = valor
    self.minimo = minimo
    self.prox = prox


class PilhaComMinimo:

  def __init__(self):
    self.topo = None

  def push(self, x):
    min_atual = x if not self.topo else min(x, self.topo.minimo)
    novo = No(x, min_atual, self.topo)
    self.topo = novo

  def pop(self):
    if not self.topo:
      return None
    val = self.topo.valor
    self.topo = self.topo.prox
    return val

  def min(self):
    return self.topo.minimo if self.topo else None

p = PilhaComMinimo()
p.push(5)
p.push(3)
p.push(7)
p.push(1)
p.pop()
print("Mínimo atual:", p.min())