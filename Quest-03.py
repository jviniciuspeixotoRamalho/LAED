#Questão 3

v = [9, 42, 21, 14, 25, 3, 19, 33, 45, 6]

while True:
  try:
    k = int(input("Digite um número inteiro k: "))
    break
  except ValueError:
    print("Entrada inválida! Digite um número inteiro!")

pos, dif = 0, 0
achou = False

for i in range(0, len(v)):
  if v[i] == k:
    print(f"O valor k = {k} foi primeiro encontrado em {v} na posição {i+1}.")
    achou = True
    break
  elif dif == 0:
    dif = abs(v[i] - k)
  elif abs(v[i] - k) < dif:
    dif = abs(v[i] - k)
    pos = i

print(f"O número buscado não se econtra na lista, o mais próximo de {k} é {v[pos]}")
