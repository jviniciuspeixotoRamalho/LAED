#Questão 4

v = [9, 2, 7, 7, 2, 2, 1, 7, 7, 9]

i, cont, impar, impar_rep = 0, 0, 0, 0

while i < len(v):
  if v[i] % 2 != 0:
    impar = v[i]
    if impar == impar_rep:
      i += 1
      continue
    cont = 1
    j = i+1
    #print(f"L1: v[{i}] = {v[i]}, cont = {cont}, j = {j}")

    while j < len(v):
      if impar == v[j]:
        cont += 1
        #print(f"L2: v[{j}] = {v[j]}, cont = {cont}, j = {j}")
      j += 1

  if cont % 2 != 0:
      break
  else:
    impar_rep = impar
  i += 1


if impar == 0:
  print(f"Não foram encontrado números ímapra na lista L = {v}.")
elif cont == 1:
  print(f"O número {impar} aparece uma vez em L = {v}.")
else:
  print(f"O número {impar} aparece {cont} vezes em L = {v}.")