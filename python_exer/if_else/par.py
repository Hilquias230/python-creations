soma = 0
for num in range(1,7):
    num = int(input('Digite o número: '))
    soma += num
if soma % 2 == 0:
    print('PARABÉNS! A soma dos números pares é {}'.format(soma))
else:
    print('A soma dos números deu ímpar, tente de novo')
    
    
