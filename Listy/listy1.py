# x = list(range(5))
# for item in x:
#   print(item)

# LEN OD LISTY ZWRACA JEJ DŁUGOŚĆ

# print(len(x))

# for i in range(len(x)):
#   print(x[i])

# deklaracja listy i iteracja poliście:

# L = [3, 5, 8, 13, 17, 27]

# for ietm in L:
#   print(elem, end=" ")

# print("\n")

# for i in range(len(L)):
#   print(L[i], end=" ")

# funkcje w listach

# K = [4, 7, 5, 7, 3, 3, 2, 8, 7]
# # print(K)

# K.append(3)
# print(K)
# print(K.count(7))
# print(K.index(7))
# K.insert(2,4)
# print(K)
# # pytanie - jak wstawić "4" na koniec listy?
# K.insert(len(K),4) # lub poprostu append()
# print(K)
# K.pop() # pop() domyślnie usuwa ostatni albo podany element
# print(K)
# K.reverse()
# print(K)
# K.sort() # lub sort(reverse=True) sortuje malejąco
# print(K)

# # Zadanie - usuń z listy wszystkie 7

# # sposób 1
# for i in range(K.count(7)):
#   K.remove(7)
# print(K)

# # sposób 2
# for i in range(K.count(7)):
#   K.pop(K.index(7))
# print(K)

# # poszukaj maksa w tablicy 2 metodami

# # sposób 1
# print(max(K))

# # sposób 2
# maksik = K[0]
# for i in K:
#   if i>maksik:
#     maksik = i
# print(maksik)

# # sposób 3
# maksik = K[0]
# for i in range(len(K)):
#   if K[i]>maksik:
#     maksik=K[i]
# print(maksik)


# zakresy w listach
M = [3, 7, 2, 1, 5, 4, 2, 4, 8, 6]

print(M[7]) # 4
print(M[1:4]) # [7, 2, 1, ]
print(M[:3]) # [3, 7, 2]
print(M[7:]) #  [4, 8, 6]
print(M[5::2]) #  [4, 4, 6]
print(M[5:3]) - nic # []
print(M[5:3:-1]) # [4, 5]
print(M[:2:-3]) # [6, 2, 1]
print(M[::-3]) # [6, 2, 1, 3]