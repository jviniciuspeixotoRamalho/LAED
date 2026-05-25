#Questão 8

u = [19, 33, 7, 7, 2, 2, 1, 7, 7, 9]
v = [2, 15, 19, 12, 33, 9, 17, 41, 54, 8]

achado, start = 0, 0

for i in range(len(u)):
  for j in range(len(v)):
    if v[i] == u[j] and start == 0:
      print(f"{v[i]}",end="")
      start = 1
      achado = v[i]
      break
    elif v[i] == u[j] and v[i] != achado:
      print(f", {v[i]}",end="")
      achado = v[i]
      break
print(".")