#Questão 5 (b)

v = [3, 6, 9, 14, 19, 21, 25, 33, 42, 45]

dec, cres, achou = False, False, False
i = 0

while i < len(v):
  if v[i] < v[i+1]:
    cres = True
    break
  elif v[i] > v[i+1]:
    dec = True
    break
  i += 1

if not dec and not cres:
  print("A lista é constante!")
elif dec:
  for i in range(len(v)-1):
    j = i + 1
    if achou:
      break
    for j in range(i+1, len(v)):
      if v[i] / v[j] == 2:
        print(f"v[{i}] = {v[i]} é o dobro de v[{j}] = {v[j]}.")
        achou = True
        break
      elif v[j] < 2*v[i]:
        break
elif cres:
  for i in range(len(v)-1):
    j = i + 1
    if achou:
      break
    for j in range(i+1, len(v)):
      if v[j] / v[i] == 2:
        print(f"v[{i}] = {v[i]} é o dobro de v[{j}] = {v[j]}.")
        achou = True
        break
      elif v[j] > 2*v[i]:
        break

if not achou:
  print("Não há na lista ordenada elemento que seja o dobro do outro!")
