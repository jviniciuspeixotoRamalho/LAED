#Questão 01

v = [9, 42, 21, 14, 28, 3, 19, 32, 46, 6]

impar, maior_impar = 0, 0
i = 0

while i < len(v):
  if v[i] % 2 != 0:
    impar = v[i]
    if impar > maior_impar:
      maior_impar = impar
  i += 1

if impar != 0:
  print(f"O maior ímpar em {v} é: {maior_impar}")
else:
  print(f"Não há ímpares na lista!")