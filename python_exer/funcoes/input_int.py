def input_int(n):
    while True:
        try:
            return int(input(n))
        except:
            print("Expressão inválida!")

