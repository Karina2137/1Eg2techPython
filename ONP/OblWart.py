# Algorytm obliczający wartość ONP
s = input()
stos = []
for elem in s:
  if elem.isdigit(): stos.append(int(elem))
  else:
    b, a = stos.pop(), stos.pop()
    if elem == "+" : stos.append(a+b)
    elif elem == "*" : stos.append(a*b)
    elif elem == "-" : stos.append(a-b)
    elif elem == "/" : stos.append(a//b)
  print(stos)
print(stos)