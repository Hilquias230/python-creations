print("Informe três números e descubra o maior e o menor")
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if (num1 > num2 > num3):
    print(f"O maior é {num1} e o menor é {num3}")
elif (num3 > num2 > num1):
    print(f"O maior é {num3} e o menor é {num1}")
elif (num2 > num1 > num3):
    print(f"O maior é {num2} e o menor é {num3}")
elif (num3 > num1 > num2):
    print(f"O maior é {num3} e o menor é {num2}")