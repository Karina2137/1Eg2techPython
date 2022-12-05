# Funkcja ord() - zwraca kod ascii dla danego znaku
# print(ord("A"))
# print(ord("B"))
# print(ord("Z"))

# Funkcja chr() - zwraca znak dla danego kod ascii  
# print(chr(65))
# print(chr(75))
# print(chr(89))

# można łączyć
# print(chr(ord("C")))


#  Alfabet
# for i in range(65,91):
#   print(chr(i), end="")


# napis = int(input())
# for i in range(len(napis)):
#   print(napis[i])

# Szyfr  Cezara
napis = input()
szyfr=""
for i in range(len(napis)):
  szyfr= szyfr + (chr(ord(napis[i]) - 65 + 3) % 26)
print(napis, szyfr)