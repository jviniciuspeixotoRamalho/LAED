#Questão 4

v = [17, 2, 8, 1, 7, 13, 9, 12, 4, 16]

t1, t2 = False, False

for i in range(len(v)-1):
  k = v[i]
  for j in range(i+1, len(v)):
    if v[j] == k+1:
      t1 = True
    elif v[j] == k-1:
      t2 = True
    elif t1 and t2:
      break

print(f"O elemento isolado da lista é: {k}.")