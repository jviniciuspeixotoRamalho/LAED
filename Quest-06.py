#Questão 6

v = [3, 6, 9, 14, 19, 21, 25, 33, 42, 45]

achou = False

while True:
  try:
    k = int(input("Digite a diferença máxima entre dois inteiros: "))

    if k > 0:
      break
    else:
      print("O número digitado deve ser um número inteiro positivo!")

  except ValueError:
    print("O número digitado deve ser um número inteiro positivo!")

for i in range(len(v)-1):
 
  for j in range(i+1, len(v)):
    if achou:
      break
    if abs(v[i] - v[j]) == k:
      print(f"Os números {v[i]} e {v[j]} diferem entre si em valor absoluto igual a {k}.")
      achou = True
      break

if not achou:
  print(f"Não há na lista L = {v} elementos que difiram entre si em valor absoluto igual a {k}.")
