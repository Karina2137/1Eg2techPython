# Algorytm Zachłanny
T=[50,20,10,5,2,1]
x = int(input())

for i in T:
  ilosc=x//T[i]
  if ilosc > 0:
    x -= ilosc*T[i]
    print(f"Nominał{i} ilosc{T[i]})