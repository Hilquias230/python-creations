num = int(input("Digite o número: "))
x = 0
fato = 1

for x in range(num, 1, -1):
    fato *= x

print(fato)