# Zad.1

a = int(input("Podaj a:"))
if a%3==0:
  print("TAK")
else:
  print("NIE")

#Zad.2

a = int(input("Podaj a:"))
if a>=100 and a<1000 and a%17==0:
    print("TAK")
else:
  print("NIE")
#Zad.3
wiek = int(input("podaj wiek:"))
if wiek>=18:
  print("TAK")
else:
  print("NIE")

#Zad.4

limit = int(input("Podaj masę pojazdu:"))
if limit>=20:
  print("Nie możesz wjechać")
else:
  print("Tak możesz wjechać")

#Zad.5

a, b, c = map(int, input().split())
if(a < c and b>c) or (b < c and a > c):
 print("Tak")
else:
  print("Nie")

#Zad.6

a = int(input("Podaj dowolną liczbę"))
p = int(input("Podaj liczbę pierwszą"))
if ((a**2 - a) % p) == 0:
  print("tak spełnia MTF")
else:
  print("Nie spełnia")


#Zad.7

p, k, s = map(int, input().split())
if 3*s + p >= k:
  print("Tak")
else:
  print("Nie")