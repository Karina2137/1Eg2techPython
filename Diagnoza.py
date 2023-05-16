# Diagnoza INF

# - WSTĘP
# 1. Oblicz sumę liczb 3-cyfrowych

suma1 = 0
for i in range(100,1000):
  suma1 += i
print(suma1)

# 2. Oblicz sumę i ilość dwucyfrowych wielokrotności liczby 6

suma2=0
ilosc1=0
for i in range(10,100):
  if i % 6 == 0:
    suma2+=i
    ilosc1+=1
print(suma2,ilosc1)

# 3. Znajdź największą liczbę wśród 5 wylosowanych przez program liczb 4-cyfrowych
import random
A = [random.randint(1000,10000) for i in range(5)]
maks = 0
for i in range(5):
  if A[i] > maks:
    maks =A[i]
print(A)
print(maks)

# 4. Podaj sumę cyfr w dowolnej liczbie

k = int(input())
suma3=0
while (k>0):
  suma3+=k%10
  k= k//10
print(suma3)

# 5. Znajdź najmniejszą cyfrę we wpisanej przez usera liczbie 3-cyfrowej

l=int(input())
maks2=0
l1=l%10
l2=(l//10)%10
l3=l//100
if l1 < l2 and l1 < l3:
  print(l1)
else:
  if l2 < l1 and l2 < l3:
    print(l2)
  else:
    print(l3)

# - ALGORYTMY
# 1. Sprawdź czy wpisana przez usera liczba jest pierwsza



# 2. Sprawdź czy wpisana przez usera liczba jest złożona



# 3. Sprawdź czy wpisana przez usera liczba jest względnie pierwsza z 24



# 4. Zakoduj szyfrem CEZARA i kluczem k słowo s.



# 5. Dodaj dwa ułamki a/b + c/d. Zapisz sumę jako ułamek nieskracalny i liczbę mieszaną.



# 6. Znajdź NWW dwóch wpisanych przez usera liczb




# - KARTKA
# 1. Oblicz wartość ONP - 8822+/234*---
# 2. Znajdź postać ONP dla pisanego wyrażenia - (3+8)/4-6*(3*4/2)
# 3. Napisz na kartce algorytm NWD (obie wersje) i przeprowadz symulacje kroków dla podanych liczb - dowolny i a=35 b=56

# - NAPISY
# 1. Znajdź ilość liter C we wpisanym napisie



# 2. Sprawdź czy literki w napisie są w porządku nierosnącym: np ZOO, WOK, WODA itp



# 3. Podaj najdłuższy z 3 wpisanych przez usera wyrazów.


