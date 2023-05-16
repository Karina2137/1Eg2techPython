# print("Zadanie 1")
# Wczytaj dowolny napis i wypisz z niego pierwszą i ostatnią literkę

# a = input()
# print(f"{a[0]} i {[len(a)-1]}")
# print(f"{a[0]} i {a[-1]}")

# print("Zadanie 2")
# 2. Wczytaj dowolny napis i wypisz z niego literki bez pierwszej i ostatniej

# b = input()
# print(b[1:-1])
# print(b[1:[len(b)-1]])
# for i in range(1, len(b)-1):
#   print(b[i],end="")
# print()

# print("Zadanie 3")
# 3. Wypisz 4 ostatnie literki z wpisanego napisy w kolejności od końca

# c = input()
# print(c[-1:-5:-1])
# print(c[:-5:-1])
# for i in range(len(c)-1, len(c)-5, -1):
#   print(c[i], end="")

# C=list(c)
# C.reverse();
# c = "".join(C)
# print(C[:-4])

# print("Zadanie 4")
# 4. Waga napisu to suma kodów ascii jego liter. Zważ wpisny napis

# d = input()
# s = 0
# for i in d:
#   s += ord(i) 
# print(s)

# print("Zadanie 5")
# 5. Policz ile we wpisanym napisie jest liter A.

# e = input()
# ilosc = 0 
# for x in e:
#   if x == "A":
#     ilosc += 1
# print(ilosc)

# print("Zadanie 6")
# 6. Podaj dominującą literkę we wpisanym napisie. 
# Niech to będzie tylko jedna literka.

# f = input()
# maks = 0
# for i in f:
#   if f.count(i) > maks:
#     maks = f.count(i)
#     litera = i
# print(f'{litera} {maks}')

print("Zadanie 7")
# 7. Znajdź literkę-dominantę w napisie (może ich być kilka, a może nie być żadnej)

# def czyJestMniejszyNiezerowy(L):
#   for i in L:
#     if 0 < L.count(i) < max(L):
#       return True
#   return False

# g = input()
# Z = [0] * 100
# for i in g:
#   Z[ord(i)] += 1
# print(Z)
# domikand = max(Z)

# if sum(Z) == max(Z):
#   print(f"Dominanta {chr(Z.index(max(Z)))}")

# elif not czyJestMniejszyNiezerowy(Z):
#   print("Brak dominanty")
# else:
#   D = []
#   for i in range(len(Z)):
#     if Z[i] == max(Z):
#       D.append(chr(i))
#   print("Dominanty:",", ".join(D))

print("Zadanie 8")
# 8. Sprawdź czy w napisie występują trzy podciągi "LA"
# TIP: h[i:i+2] == "LA"
h = input()

print("Zadanie 9")
# 9. Znajdź "średnią literkę" w napisie. (Przejdź na kody ASCII i jeśli wynik będzie ułamkowy to zaokrąglij średnią w dół)

i = input()

print("Zadanie 10")
# 10. Wypisz literki, których nie ma w napisie

j = input()

print("Zadanie 11")
# 11. Znajdź ilość trzyznakowych palindromów w napisie (trzy literki koło siebie)