#Algorytm zamiany liczb z systemui 10 na 2
#Itteracyjnie
def dec2bin(n):
    w=""
    while n>0:
        w = str(n//2) + w
        n//=2
    return w
print(dec2bin(37))

#Rekurencyjnie
def dec2binreku1(n):
    if n ==0:
        return ""
    return dec2binreku1(n//2) + str(n%2)

def dec2binreku2(n):
    if n ==0:
        return
    dec2binreku2(n//2)
    print(n%2, end="")

print(dec2bin(39))
print(dec2binreku1(39))
dec2binreku2(39)


#Algorytm zamiany liczb z systemui 2 na 10
#Schemat Hornera -- można, nie trzeba
def bin2dechorner(n):
    w = 0
    for i in range(len(n)):
        w = w*2 + int(n[i])
    return w

#Itteracyjnie
def bin2dec1(n):
    s = 0
    for i in range(len(n)):
        s = s + 2**i * int(n[-i-1])
    return s

#Rekurencyjnie


print("\n")
print(bin2dechorner("10011"))
print(bin2dec1("10011"))
