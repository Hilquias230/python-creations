
continua= ['S','N']
num=0
numeros=[ ]

while True:
    num=int(input('Digite um número: '))
    numeros.append(num)
  
    
    if len(numeros) > 0:
        media=sum(numeros) / len(numeros)
        maior=max(numeros) 
        menor=min(numeros)
        
    continua=str(input('Quer continuar?[S/N]:  ')).strip().upper()
    if continua == 'S':
        pass
    elif continua=='N':
        break

print(f'O maior é {maior} e o menor é {menor}')
print(f'A média é {media}')

   
