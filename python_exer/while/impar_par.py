import random
from time import sleep
comp= ['impar','par']
jog=1
cont=0
acum=1
print('Pense em impar ou par...')
print('::'*50)
while jog != 'n':
    sleep(2)
    print(f'Você pensou em {random.choice(comp)}?')
    jog=str(input('Responda(s ou n):'))
    if jog != 'n' :
        cont += acum
    elif jog == 'n':
        break
    elif jog == 's':
        continue
print('::'*50)
print('Ah que pena :(')
print(f'Acertei apenas {cont} vezes')
        
    

