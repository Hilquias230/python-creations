sal = float(input("Informe o salário: "))

if (sal <= 1903.98):
    imposto = 0
elif (sal <= 1903.99):
    imposto = sal * 7.5 / 100
elif (sal <= 3751.05):
    imposto = sal * 15 / 100
elif (sal <= 4664.68):
    imposto = sal * 22.5 / 100
else:
    imposto = sal * 27.5 / 100
print(f"O seu imposto de renda deu {imposto}")     

