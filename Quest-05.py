#Questão 5

v = [7, 1, 9, 1, 7, 3, 9, 2, 1, 6, 8, 3, 2, 6, 8, 13]
u = []

achou = False


while True:
  try:
    k = int(input(f"Digite um número entre 1 e {len(v)}: "))
    if 0 < k <= len(v):
      break
    else:
      print(f"Entrada inválida! Deve ser um número deve estar entre 1 e {len(v)}.")
  except ValueError:
    print(f"Entrada inválida! Deve ser um número deve estar entre 1 e {len(v)}.")

for i in range(len(v)):
  cont = 1
  #Comparação
  for j in range(i+1, len(v)):
    if v[i] == v[j]:
      cont += 1

  #Verificação
  if k != cont:
    u.append(v[i])
  else:
    t = 0
    teste = False
    while t < len(u):
      if u[t] == v[i]:
        teste = True
        break
      t +=1
    if not teste:
      achou = True
      x = v[i]
      break


if not achou:
  print(f"Não há na lista elemento com {k}-vez(es) ocorrências nesta!")
else:
  print(f"O elemento {x} ocorre {k}-vez(es) na lista.")