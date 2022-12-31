# Zad 1

# n = int(input())
# suma = 0
# while n > 0:
#     suma = suma + n%10
#     n = n // 10
# print(suma)

# Zad 2

# n = int(input())
# for i in range(2,n):
#   if n%i==0:
#     print("Liczba nie jest pierwsza")
#     exit(0)
# print("Liczba jest pierwsza")

# Zad 3 - 6 28 496 8128 

# n = int(input())
# suma = 0
# for i in range(1,n):
#     if n % i == 0:
#         suma += i
# if suma == n:
#     print("Liczba jest doskonała")
# else:
#     print("Nie jest doskonała")

# Zad 4

# x = int(input())
# y = int(input())
# while y > 0:
#   x, y = y, x % y
# if x==1:
#   print("TAK")
# else:
#   print("NIE")

# Zad 5

# n = int(input())

# for i in range(10,20):
#     x = n
#     y = i
#     while y > 0:
#         x, y = y, x % y
#     if x == 1:
#         print(f"Mamy parkę: {n}, {i}")

# Zad 6

# a = int(input())
# b = int(input())

# x, y = a, b
# while x!=y:
#     if x>y: x -= y
#     if y>x: y -= x

# c = a//x
# d = b//x

# print(f"{a}/{b} = {c}/{d}")

# Zad 7

