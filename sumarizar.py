lista_n = []

while True:
    num = int(input("Digite um número para acrescentar na lista: "))
    lista_n.append(num)
    conf = str(input("Deseja continuar?[S/N]: ")).upper()
    if (conf == "N"):
        break
    elif (conf == "S"):
        continue

print("Pecorrendo a lista para ver algum número repetido...")

dic_num = {}

for cont in lista_n:
    if cont in dic_num:
        dic_num[cont] += 1
    else:
        dic_num[cont] = 1

for n, vezes in dic_num.items():
    print(f"Número {n}: {vezes} vezes")

