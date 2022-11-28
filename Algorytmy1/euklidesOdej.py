# Obliczanie NWD
a, b = int(input()), int(input())
while a != b:
  if a > b: a -= b
  if a < b: b -= a
print(a)