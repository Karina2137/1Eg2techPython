# Obliczanie NWW
a, b = int(input()), int(input())
c = a*b
while b > 0:
  a, b = b, a % b
print("NWW =", c//a)