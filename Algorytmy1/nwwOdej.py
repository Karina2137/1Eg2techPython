# Obliczanie NWW
a, b = int(input()), int(input())
c = a*b
while a != b:
  if a > b: a -= b
  if a < b: b -= a
print("NWW =", c//a)