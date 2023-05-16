# # Diagnoza INF

# # - WSTĘP
# print("WSTĘP")
# # 1. Oblicz sumę liczb 3-cyfrowych
# print("Zadanie 1")
# suma1 = 0
# for i in range(100,1000):
#   suma1 += i
# print(suma1)
# print()
# # 2. Oblicz sumę i ilość dwucyfrowych wielokrotności liczby 6
# print("Zadanie 2")
# suma2=0
# ilosc1=0
# for i in range(10,100):
#   if i % 6 == 0:
#     suma2+=i
#     ilosc1+=1
# print(suma2,ilosc1)
# print()
# # 3. Znajdź największą liczbę wśród 5 wylosowanych przez program liczb 4-cyfrowych
# print("Zadanie 3")
# import random
# A = [random.randint(1000,10000) for i in range(5)]
# maks = 0
# for i in range(5):
#   if A[i] > maks:
#     maks =A[i]
# print(A)
# print(maks)
# print()
# # 4. Podaj sumę cyfr w dowolnej liczbie
# print("Zadanie 4")
# k = int(input())
# suma3=0
# while (k>0):
#   suma3+=k%10
#   k= k//10
# print(suma3)
# print()
# # 5. Znajdź najmniejszą cyfrę we wpisanej przez usera liczbie 3-cyfrowej
# print("Zadanie 5")
# l=int(input())
# maks2=0
# l1=l%10
# l2=(l//10)%10
# l3=l//100
# if l1 < l2 and l1 < l3:
#   print(l1)
# else:
#   if l2 < l1 and l2 < l3:
#     print(l2)
#   else:
#     print(l3)
# print()

# # - ALGORYTMY
# print("ALGORYTMY")
# # 1. Sprawdź czy wpisana przez usera liczba jest pierwsza
# print("Zadanie 1")
# m = int(input())
# for i in range(2,m-1):
#   if m % i == 0:
#     print(f"Liczba {m} nie jest pierwsza")
#     break
#   else:
#     print(f"Liczba {m} jest pierwsza")
# print()
# # 2. Sprawdź czy wpisana przez usera liczba jest złożona
# print("Zadanie 2")
# n = int(input())
# for i in range(2,n-1):
#   if n % i == 0:
#     print(f"Liczba {n} jest złożona")
#   break
# print(f"Liczba {n} nie jest złożona")
# print()
# # 3. Sprawdź czy wpisana przez usera liczba jest względnie pierwsza z 24
# print("Zadanie 3")
# o = int(input())
# a = o
# b = 24 
# c = o * 24
# while b > 0:
#   a, b = b, a % b
# if a == 1:
#   print(f"Liczba {o} jest względnie pierwsza z 24")
# else:
#   print(f"Liczba {o} nie jest względnie pierwsza z 24")
# print()
# # 4. Zakoduj szyfrem CEZARA i kluczem k słowo s.
# print("Zadanie 4")
# s = input()
# k = int(input())
# szyfr = ""
# for i in range(len(s)):
#   szyfr = szyfr + chr(65 + (ord(s[i]) - 65 + k) % 26)
# print(s, szyfr)
# print()
# # 5. Dodaj dwa ułamki a/b + c/d. Zapisz sumę jako ułamek nieskracalny i liczbę mieszaną.
# print("Zadanie 5")
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# g = b
# h = d
# i = b*d
# while h > 0:
#   g, h = h, g % h
# nww = i//g
# e = (nww // b) * a
# f = (nww // d) * c
# j = e + f
# k = j // nww
# l = j % nww
# if j < nww:
#   print(f"{a}/{b} + {c}/{d} = {e}/{nww} + {f}/{nww} = {j}/{nww}")
# else:
#   print(f"{a}/{b} + {c}/{d} = {e}/{nww} + {f}/{nww} = {j}/{nww} = {k} {l}/{nww}")
# print()
# # 6. Znajdź NWW dwóch wpisanych przez usera liczb
# print("Zadanie 6")
# p, r = int(input()), int(input())
# q = p * r
# nww = 0
# while r > 0:
#   p, r = r, p % r
# nww = q // p
# print(nww)
# print()

# # - KARTKA
# # 1. Oblicz wartość ONP - 8822+/234*---
# # 2. Znajdź postać ONP dla pisanego wyrażenia - (3+8)/4-6*(3*4/2)
# # 3. Napisz na kartce algorytm NWD (obie wersje) i przeprowadz symulacje kroków dla podanych liczb - dowolny i a=35 b=56


# # - NAPISY
# print("NAPISY")
# # 1. Znajdź ilość liter C we wpisanym napisie
# print("Zadanie 1")
# napis = input()
# ilosc = 0
# for i in range(len(napis)):
#   if napis[i] == "C":
#     ilosc += 1
# print(ilosc)
# print()
# # 2. Sprawdź czy literki w napisie są w porządku nierosnącym: np ZOO, WOK, WODA itp
# print("Zadanie 2")
# napis = input()
# nr = 0
# for i in range(len(napis)-1):
#    if ord(napis[i]) >= ord(napis[i+1]):
#      nr += 1
# if nr == len(napis)-1:
#   print(f"Literki w napisie {napis} są w porządku nierosnącym")
# else:
#   print(f"Literki w napisie {napis} nie są lub nie wszystkie są w porządku nierosnącym")
# print()
# 3. Podaj najdłuższy z 3 wpisanych przez usera wyrazów.
# print("Zadanie 3")
# x, y, z = input(), input(), input()
# x1, y1, z1 = len(x), len(y), len(z)
# if x1 > y1 and x1 > z1:
#   print(f"Najdłuższy jest {x}")
# else:
#   if y1 > x1 and y1 > z1:
#     print(f"Najdłuższy jest {y}")
#   else:
#     print(f"Najdłuższy jest {z}")
# print()