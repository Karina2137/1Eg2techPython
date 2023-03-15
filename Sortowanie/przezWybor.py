# Wygenerój losową listę 7 elementów z przedziału (1,20)

from random import randint
n = 17
L = [randint(1,100) for i in range (n)]
print(L)

for i in range(n):
  mi = i
  for j in range(i+1,n):
    if L[j] < L[mi]:
      mi = j 
  # L[i] <-> L[mi]
  L[i], L[mi] = L[mi], L[i]
print(L)