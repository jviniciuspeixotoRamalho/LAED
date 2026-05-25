#Questão 5 (a)

v = [9, 42, 21, 14, 25, 3, 19, 33, 45, 6]

i = 0
achou = False

while i < len(v):
  j = i+1
  while j < len(v):
    if v[j] / v[i] == 2:
      print(f"v[{j}] = {v[j]} é o dobro de v[{i}] = {v[i]}.")
      achou = True
      break
    j +=1
  i += 1

if not achou:
  print("Não há elemento na lista que seja o dobro do outro!")