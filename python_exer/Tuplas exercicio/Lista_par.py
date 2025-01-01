lista= []
par = []
impar = []


while True:
    num=int(input('Digite o número: '))
    lista.append(num)
    
    if num == 0:
        break
    
    if num %2==0:
        par.append(num)
    else:
        impar.append(num)

        
print('='*30)
print(f'Essa é a lista total:' )
print(lista)       
print('='*30)
print(f'Essa é a lista par:')
print(par)
print('='*30)
print('Essa é a lista de impar:')
print(impar)
print('='*30)
