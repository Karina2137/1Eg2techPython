#Ankieta

# x = int(input("Podaj liczbę"))
# z = int(input("Podaj drugą liczbę"))
# if (1.3*z > x):
#   print("TAK")
# else:
#   print("NIE")

#Zad.1
# a = int(input())
# for i in range(a):
#   print(i**3 + 3, end=" ")

#Zad.2
# for i in range(105,1000,15):
#   print(i, end=" ")

#Zad.3
# n = int(input())
# for i in range(1,n+1):
#   if n % i == 0:
#     print(i, end=" ")

#Zad.4
# suma = 0
# for i in range(10,100):
#   suma = suma + i
# print(suma)

#Zad.5
# n = int(input())
# suma = (n*(n+1)//2)

# for i in range(n-1):
#   x = int(input())
#   suma = suma - x
# print("Nie podałeś:",suma)

# Zad.6
# a = 0
# b = 1
# n = int(input("Podaj ile razy:"))
# print(a,end=" ")
# print(b,end=" ")
# for i in range(n-2):
#   a, b = b, a+b
#   print(b, end=" ")


# pętla liczb dwucyfrowych od 10 do 21
# for i in range(10,22): print(i, end=" ")

# pętla liczb dwucyfrowych nieparzystych od 15 do 31  
# for i in range(15,32, 2): print(i, end=" ")

# pętla liczb dwucyfrowych malejąco (step ujemny)
# for i in range(99,10,-1): print(i, end=" " )

# pętla liczb dwucyfrowych malejąco (step dodatni)
# for i in range(10,100,1): print(109-i, end=" ")

# pętla liczb 3-cyfrowych podzielnych przez 20
# for i in range(100,999,20): print(i, end=" ")



# POST - utrwalenie pętli

# Pętle for liczb trzycyforowych podzielnych przez 13 (2 sposoby)
# for i in range(104,1000,13):
#   print(i, end=" ")

# for i in range(100,1000):
#   if i % 13 == 0:
#     print(i, end=" ")


# Pętle for liczb dwucyfrowych parzystych (3 sposoby)
# for i in range(10,99,2): 
#   print(i, end=" ")

# for i in range(10,100):
#  if i % 2 == 0:
#     print(i, end=" ")

# for i in range(5, 50):
#   print(i * 2, end=" ")


# Pętle for potęg cyfr: WY: 0, 1, 4, 9, 16 .. 81 (2 sposoby printa)

# for i in range(10):
#   print(i ** 2)
  
# for i in range(10):
#   print(f"i^2 = {i ** 2}")
  
# for i in range(10):
#   print(i,"^2=",i** 2)
  
# for i in range(10):
#   print(i,"^2=",i** 2, sep="")