#Questão 7

v = [9, 2, 7, 7, 2, 2, 1, 7, 7, 9]

i, inv, aux = 0, 0, 0

print(f"Iniciando lista: L = {v}.\n")

while i < len(v) - 1:
  j = i + 1
  while j < len(v):
    if v[i] > v[j]:
      inv += 1
      aux = v[i]
      v[i] = v[j]
      v[j] = aux
    j += 1
  i += 1

print(f"Número de inversões: {inv}.\nFinalizando lista: L = {v}.")