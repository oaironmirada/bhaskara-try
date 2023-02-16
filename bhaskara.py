import math

def calculate_delta(a, b, c):
    return b**2 - 4*a*c

def calculate_roots(a, b, c):
    delta = calculate_delta(a, b, c)
    if delta < 0:
        print("A equação não possui raizes reais")
        return None
    elif delta == 0:
        print("A equação possui apenas um resultado real ou possui dois resultados iguais")
        x = -b / (2*a)
        return x
    else:
        print("A equação possui duas raizes reais")
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2

def determine_concavity(a):
    if a < 0:
        print("A concavidade da figura será voltada para baixo")
    else:
        print("A concavidade da figura será voltada para cima")

def calculate_vertex(a, b):
    vx = -b / (2*a)
    vy = calculate_delta(a, b, 0) / (4*a)
    return vx, vy

def get_coefficients():
    a = int(input("Digite o coeficiente a: "))
    b = int(input("Digite o coeficiente b: "))
    c = int(input("Digite o coeficiente c: "))
    return a, b, c

def main():
    a, b, c = get_coefficients()

    roots = calculate_roots(a, b, c)
    if roots is not None:
        print(f"As raízes são: {roots}")

    determine_concavity(a)

    vertex = calculate_vertex(a, b)
    print(f"O vértice é: {vertex}")

if __name__ == '__main__':
    main()
