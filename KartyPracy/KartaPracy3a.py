#Zad.1
# n = int(input("Podaj n:"))
# for i in range(n):
#   print("*-|", end="")

#Zad.2
# n = int(input())
# for i in range(1,n+1):
#   print("*"*i, end="")
#   if i%2:
#     print("||",end="")
#   else:
#     print("--",end="")

# Zad.3
# n = int(input())
# for i in range(1,n+1):
#   print("*", end="")
#   if i%2==1:
#     print("|"*i, end="")
#   else:
#     print("-"*i, end="")

# PRE - Tabliczka mnoZenia
# for i in range(1,11):
#   for j in range(1,11):
#     print(i*j, end="\t")
#   print()

# PRE na 2 pętle

# (1,1)(1,2)(1,3)(1,4)(1,5)
# (2,1)(2,2)(2,3)(2,4)(2,5)
# (3,1)(3,2)(3,3)(3,4)(3,5)
# (4,1)(4,2)(4,3)(4,4)(4,5)
# (5,1)(5,2)(5,3)(5,4)(5,5)

# *
# **
# ***
# ****

# ****
# ***
# **
# *

# n = int(input())
# for i in range(n):
#   for j in range (i+1):
#     print("*",end="")
#   print()

# print()
# print()

# for i in range(n):
#   for j in range (n-i):
#     print("*",end="")
#   print()


#    *
#   **
#  ***
# ****

# ****
#  ***
#   **
#    *

# print()
# print()

# for i in range(n):
#   for j in range(n-i):
#     print("*", end="")
#   print()

# print()
# print()

# for i in range(n):
#   for j in range(n-i-1):
#     print("*", end="")
#   for k in range(n-i-1, n):
#     print("*",end="")
#   print()

# print()
# print()

# for i in range(n):
#   for j in range(i):
#     print(" ",end="")
#   for k in range(i, n):
#     print("*",end="")
#   print()

# n = int(input())


# *
# **
# ***
# ****

# for i in range(n):
#   for j in range(n):
#     if i>=j:
#       print("*", end="")
#     else:
#       print(" ", end="")
#   print()

# print()
# print()

# # ****
# #  ***
# #   **
# #    *

# for i in range(n):
#   for j in range(n):
#     if j>=i:
#       print("*", end="")
#     else:
#       print(" ", end="")
#   print()

# print()
# print()

# PRE INNA METODA:

# # *
# #  *
# #   *
# #    *

# for i in range(n):
#   for j in range(n):
#     if i==j:
#       print("*", end="")
#     else:
#       print(" ", end="")
#   print()

# print()
# print()

#    *
#   *
#  *
# *

#   for j in range(n):
#     if i+j == n-1:
#       print("*", end="")
#     else:
#       print(" ", end="")
#   print()

# print()
# print()

# for i in range(n):
#   for j in range(n):
#     if i+j == n-1:
#       print("*", end="")
#     else:
#       print(" ", end="")
#   print()

# print()
# print()

# for i in range(n):
#   for j in range(n):
#     if i == n - j - 1:
#       print("*", end="")
#     else:
#       print(" ", end="")
#   print()

# print()
# print()

#    *
#   **
#  ***
# ****

# for i in range(n):
#   for j in range(n):
#     if i >= n - j - 1:
#       print("*", end="")
#     else:
#       print(" ", end="")
#   print()

# print()
# print()



# # ****
# # ***
# # **
# # *

# for i in range(n):
#   for j in range(n):
#     if i <= n - j - 1:
#       print("*", end="")
#     else:
#       print(" ", end="")
#   print()

# print()
# print()

