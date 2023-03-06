# Anagram przez sortowanie
# a, b = input(), input()
# X, Y = list(a), list(b)
# X.sort()
# Y.sort()
# a, b = "".join(X), "".join(Y)
# print(a,b)
# if a == b:
#   print("Tak")
# else:
#   print("Nie")

# Anagram przez tablicę
a, b = input(), input()
X, Y = [0] * 150, [0] * 150
for i in range(len(a)):
  X[ord(a[i])] += 1 
for i in range(len(b)):
  Y[ord(b[i])] += 1
if X == Y:    print("Tak")
else:         print("Nie")