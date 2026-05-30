#Questão 01

v = [9, 42, 21, 14, 25, 3, 19, 33, 45, 6]

m1, m2, m3 = 0, 0, 0

if v[0] < v[1]:
  m1 = v[1]
  m2 = v[0]
elif v[0] > v[1]:
  m1 = v[0]
  m2 = v[1]

for i in range(len(v)):
  if v[i] > m1:
    m3 = m2
    m2 = m1
    m1 = v[i]
  elif m1 > v[i] > m2:
    m3 = m2
    m2 = v[i]

print(f"O terceiro maior elemento da lista é: {m3}.")