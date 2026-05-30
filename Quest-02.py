#Questão 2

v = [9, 42, 21, 14, 25, 3, 19, 33, 45, 6]

aux = 0

print(f"Lista iniciada: {v}.")

while True:
  try:
    k = int(input(f"Digite uma posição da lista entre 1 e {len(v)}: "))

    if 0 < k <= len(v):
      break
    else:
      print(f"Deve-se digitar um número inteiro positivo entre 1 e {len(v)}!\n")
  except ValueError:
      print(f"Deve-se digitar um número inteiro positivo entre 1 e {len(v)}!\n")
for  i in range(len(v)-1):
  for j in range(i+1, len(v)):
    if v[j] > v[i]:
      aux = v[j]
      v[j] = v[i]
      v[i] = aux

print(f"Lista pós-processamento: {v}.")
print(f"O {k}-ésimo maior elemento da lista é {v[k-1]}.")