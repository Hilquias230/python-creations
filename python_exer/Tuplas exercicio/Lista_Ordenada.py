from random import randint
lista=[]
while True:
    vals=randint(0,20)
    num=int(input('Digite os números:'))
    lista.append(num)
    if num == 0:
        break
if vals == num:
    print('='*30)
    print('Valor S foi digitado')
    print(f'Valor S é {vals}')
else:
    print('='*30)
    print('Valor S não foi digitado')
    print(f'O Valor S foi {vals}')

print('='*30)
lista.sort(reverse=True)
print(lista)
print(f'A lista tem {len(lista)} elementos')
print('='*30)



