def fatorial (n):
    if n <= 1:
        return 1
    return n * fatorial(n -1)

num = int(input("Digite o número: "))

print(f"O fatorial de {num} é {fatorial(num)}")
