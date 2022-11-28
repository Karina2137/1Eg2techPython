# Obliczanie NWD
# Sposób 1
a, b = int(input()), int(input())
while a != b:
  if a > b: a -= b
  if a < b: b -= a
print(a)

# Sposób 2
c, d  = int(input()), int(input())
while b > 0:
  a, b = b, a % b
print(a)