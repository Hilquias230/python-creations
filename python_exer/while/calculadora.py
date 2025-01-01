
while True:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    print("-"*100)
    print("""[1] SOMAR
[2] SUBTRAIR
[3] MULTIPLICAÇÃO
[4] DIVISÃO
[5] SAIR
        """)
    print("-"*100)
    
    op = int(input("Escolha uma das opções: "))

    if (op == 1):
        somar = num1 + num2
        print(f"A soma deu {somar}")
    elif (op == 2):
        sub = num1 - num2
        print(f"A subtração dos dois números deu {sub}")
    elif (op == 3):
        multi = num1 * num2
        print(f"A multiplicação deu {multi}")
    elif (op == 4):
        div = num1 / num2
        print(f"A divisão deu {div}")
    elif (op == 5):
        break
print("-"*100)
print("PROGAMA FINALIZADO")   
