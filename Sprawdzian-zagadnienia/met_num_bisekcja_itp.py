#Zagadnienia na spr 1:

#1. Metody numeryczne - prostokąty i trapezy 
#   (możliwie inne figury - np trójkąty i romby)
# metoda prostokątów - potrzeba jest funkcja oraz trzy warianty tej metody


def f(x): 
    return -x**2 + 6*x + 2

def prostokaty1(a, b, n):
    dx = (b - a) / n
    s = 0
    for i in range(n):
        s += f(a + i * dx) * dx
    return s

def prostokaty2(a, b, n):
    dx = (b - a) / n
    s = 0
    for i in range(n):
        s += f(a + dx / 2 + i * dx) * dx
    return s

def prostokaty3(a, b, n):
    dx = (b - a) / n
    s = 0
    for i in range(n):
            s += f(a + dx + i * dx) * dx
    return s

# metoda trapezów 
def trapezy1(a, b, n):
    dx = (b - a) / n
    s = 0
    for i in range(n):
        s += (f(a + i * dx) + f(a + (i + 1) * dx)) * dx / 2
    return s

def trapezy2(a, b, n):
    dx = (b - a) / n
    s = f(a) + f(b)
    for i in range(1,n-1):
        s += 2 * f(a + i * dx)
    return s * dx / 2

#2. Metoda bisekcji (stopowana ilością kroków lub przedziałem)
#3. Alg Newtona - Raphsona (stopowany ilością kroków lub przedziałem)
#4. Wyszukiwanie lidera w liście
#5. Metoda Monte Carlo
