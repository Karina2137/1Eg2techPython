from random import random as r 
punkty_w_kole = 0
liczba_losowan = 50
for i in range(liczba_losowan):
    x, y = r(), r()
    print(x, y)
    suma_kwadratow = x**2 + y**2
    print("Suma kwadratów: ",suma_kwadratow, end="")
    if (suma_kwadratow <=1):
        punkty_w_kole += 1
        print(". Punkt w kole.\n")
    else:
        print(". Punkt poza kołem.\n")
print("Punkty w/poza: ", punkty_w_kole, "/", liczba_losowan - punkty_w_kole)
liczba_pi =  4 * punkty_w_kole / liczba_losowan
print("Wartość pi: ", liczba_pi)

#################################################################

def MonteCarlo(n):
  import random
  k = 0 
  for i in range(n):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if x**2 + y**2 <= 1:
      k += 1
  return 4*k/n
  
print(MonteCarlo(5))
print(MonteCarlo(50))
print(MonteCarlo(500))
print(MonteCarlo(5000))
