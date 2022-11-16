# 1. Algorytm sprawdzający czy liczba jest pierwsza:
# liczba pierwsza dzieli się tylko przez 1 i samą siebie
# 2,3,5,7,9,11,13,17,19,itd
#liczba x ma swój dzielnik(i ile go ma)w przedziale[]

# WERSJA1
# n = int(input("Podaj liczbę:"))
# for i in range(2,n):
#   if n%i==0:
#     print("Liczba nie jest pierwsza")
#     exit(0)
# print("Liczba jest pierwsza") 

# # WERSJA2
# n = int(input("Podaj liczbę:"))
# flaga=True
# for i in range(2,n):
#   if n%i==0:
#     flaga=False
# if flaga==True:
#   print("Liczba jest pierwsza")
# else:
#   print("Liczba nie jest pierwsza")
# # WERSJA3
from math import sqrt
n = int(input("Podaj liczbę:"))
for i in range(2,int(sqrt(n))+1):
  if n%i==0:
    print("Liczba nie jest pierwsza")
    exit(0)
print("Liczba jest pierwsza") 

# 2. Generator liczb pierwszych - liczby pierwsze w rszedziale [p, q]



# 3. Generator liczb pierwszych - początkowe k liczb pierwszych