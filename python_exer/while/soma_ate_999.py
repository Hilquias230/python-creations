num=s=0

while num != 999:
    num=int(input("Digite um número: "))
    if num == 999:
        break
    s += num

print(f'A soma vale {s}')

