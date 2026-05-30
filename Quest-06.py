#Questão 6

v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
u = [7, 2, 3, 1, 6, 5, 9, 10, 4, 8]

cont = 0

for i in range(len(v)):
  for j in range(len(u)):
    if u[j] == v[i]:
      cont += 1
if cont == len(v) == len(u):
  print("As listas são permutações uma da outra!")
else:
  print("As listas não são permutações uma da outra!")