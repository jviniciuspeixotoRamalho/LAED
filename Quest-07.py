#Questão 7

v = [2, 1, 9, 7, 6, 3, 9, 4, 2, 6, 1, 3]

achou = False

while True:
  try:
    k = int(input(f"Digite um número inteiro entre 1 e {len(v) - 1}: "))
    if 0 < k < len(v):
      break
    else:
      print(f"Entrada inválida! Dever ser um inteiro entre 1 e {len(v) - 1}.")
  except ValueError:
    print(f"Entrada inválida! Dever ser um inteiro entre 1 e {len(v) - 1}.")

print(f"\nVerificando se há dois números repetidos a uma distância {k} um do outro:")

for i in range(len(v) - 1):
  cont = 1
  for j in range(i+1, len(v)):
    if v[i] != v[j]:
      cont += 1
    elif v[i] == v[j] and k == cont:
      print(f"Sim, o {v[i]} (nas posições {i} e {j}).")
      achou = True
      break

if not achou:
  print(f"Não há dois números repetidos a uma distância {k} um do outro na lista.")