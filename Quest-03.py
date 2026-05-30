#Questão 3

v = [5, 3, 1, 10, 2, 13, 9, 12, 4, 7]

s, med, dist, aprox = 0, 0.0, 0, 0

for i in range(len(v)):
  s = s + v[i]

med = s/len(v)
dist = abs(v[0] - med)
aprox =  v[0]

if len(v) > 2:
  i = 1
  while i < len(v):
    if abs(v[i] - med) < dist:
      dist = abs(v[i] - med)
      aprox = v[i]
    i += 1

print(f"O valor que mais se aproxima da média ({med}) na lista é {aprox}.")