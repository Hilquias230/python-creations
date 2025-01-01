
def mdc (n1, n2):
    while True:
        resto = n1 % n2
        if resto == 0:
            return n2
        n1 = n2
        n2 = resto

def mmc (n1, n2):
    return n1 * n2 // mdc (n1, n2)

def principal():
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo númer: "))

    print(f"MDC = {mdc(n1, n2)}")
    print(f"MMC = {mmc(n1, n2)}")

if __name__ == "__main__":
    principal()