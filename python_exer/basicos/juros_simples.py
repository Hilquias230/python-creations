cap = float(input("Capital: "))
taxa = float(input("Taxa: "))
temp = float(input("Tempo: "))

juros = (cap * taxa * temp) / 100

print(f"Esse é o valor do juros {juros:.2f}")