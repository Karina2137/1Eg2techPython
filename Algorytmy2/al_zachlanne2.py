# Algorytm Zachłanny
T=[50,20,10,5,2,1]
x = int(input())
W=[]
for i in T:
  ilosc=x//i
  if i > 0:
    x -= ilosc*i
    for j in range(ilosc):
      W.append(i)
    # opcjonalnie zamiast apenda w forze: W += ilosc * [i]
print(W)