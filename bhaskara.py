import math


def delta_func(a, b, c):
    a = a
    b = b
    c = c
    delta = ((b**2) - (4*a*c))
    return delta

def raiz_func(delta):
    raiz = math.sqrt(delta)
    return raiz

def raizes_func(raiz):
    raiz = raiz

    if raiz < 0:
        print("A equação não possui raizes reais")
    elif raiz == 0:
        print("A equação possui apenas um resultado real ou possui dois resultados iguais")
    elif raiz > 0:
        print("A equação possui duas raizes reais")
        
    return ' '

def x_func(delta, a, b):
    delta = delta
    a = a
    b = b
    x1 = (-(b) + delta)/(2*a)
    x2 = (-(b) - delta)/(2*a)
    return x1, x2

def concavidade_func(a):
    a = a
    if a < 0:
        print("A concavidade da figura sára voltada para baixo")
    else:
        print("A concavidade da figura sára voltada para cima")
        
    return ' '

def vertices_func(a, b, delta):
    a = a
    b = b
    delta = delta
    vx = ((- b) / (2 * a))
    xy = (-(delta) / (4 * a))
    return vx, xy

def a_func():
    a = int(input("Digite o ax²: "))
    return a

def b_func():
    b = int(input("Digite o bx: "))
    return b

def c_func():
    c = int(input("Digite o x: "))
    return c

a = a_func()
b = b_func()
c = c_func()

delta = delta_func(a, b, c)
#print('O delta é ', delta)
raiz = raiz_func(delta)
#print('A raiz quadrada é ', raiz)
#raizes = raizes_func(delta)
#print(raizes)
x = x_func(delta, a, b)
#print(x)
#concavidade = concavidade_func(a)
vertices = vertices_func(a, b, delta)
#print("As vertices são ", vertices)