#Zad.1
# n = int(input("Podaj n:"))
# for i in range(n):
#   print("*-|", end="")

#Zad.2
n = int(input())
for i in range(1,n+1):
  print("*"*i, end=" ")
  if i%2:
    print("||",end="")
  else:
    print("--",end="")

# Zad.3
