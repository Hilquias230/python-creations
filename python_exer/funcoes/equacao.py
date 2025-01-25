from math import sqrt

def equa(a, b, c):
    delta = (b**2) - (4 * a * c)

    if( a == 0) or ( delta < 0):
        return print("Não é uma Equação de 2º Grau")
    elif (delta == 0):
        x1 = b * (-1) / 2 * a
        return print(f"A raiz da euqação é {(x1, )}")
    else:
        raiz = sqrt(delta)
        x1 = (b * (-1) - raiz) / (2 * a)
        x2 = (b * (-1) + raiz) / (2 * a) 

    result = (x1, x2)
    return result

def principal():
    print("Equação de 2º Grau")
    A = float(input("Digite o número que represente a: "))
    B = float(input("Digite o número que represente b: "))
    C = float(input("Digite o número que represente c: "))
    res = equa(A, B, C)
    print(f"O resultado deu {res}")


if __name__ == '__main__':
    principal()