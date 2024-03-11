T = [1,2,1,3,1,1,4] # liderem jest 1

def lider():
    kandydat = T[0]
    ilosc = 1
    for i in range(1,len(T)):
        if ilosc == 0:
            kandydat = T[0]
            ilosc = 1
    else:
        if T[i] == kandydat:
            ilosc += 1
        else:
            ilosc -= 1
    ilosc_kandydatów = 0
    if ilosc == 0:
        print("Brak lidera")
    else:
        for i in range(len(T)):
            if T[i] == kandydat:
                ilosc_kandydatów += 1
    if ilosc_kandydatów > len(T)/2:
        print("Mamy lidera:", ilosc)
    else:
        print("Mimo kandydata brak lidera")
