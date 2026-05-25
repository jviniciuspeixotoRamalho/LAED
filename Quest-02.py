#Questão 02

v = [9, 42, 21, 14, 28, 3, 19, 32, 46, 6]

impar, maior_impar, seg_maior_impar = 0, 0, 0

for i in range(0, len(v)):
  if v[i] % 2 != 0:
    impar = v[i]

  if impar != 0 and maior_impar == 0 and seg_maior_impar == 0:
    maior_impar, seg_maior_impar = impar, impar
  elif impar > maior_impar:
    seg_maior_impar = maior_impar
    maior_impar = impar

if impar != 0:
  print(f"O segundo maior ímpar em {v} é: {seg_maior_impar}")
else:
  print(f"Não há ímpares na lista!")