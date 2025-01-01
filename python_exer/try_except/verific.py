
while True:
    try:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))

        div = n1 / n2
        print(div)
        break
    except Exception as e:
        print(f"Erro: {type(e)}")

