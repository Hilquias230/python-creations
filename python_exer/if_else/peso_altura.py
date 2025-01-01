print('Descubra a situção do seu peso')
peso=float(input('Digite seu peso: '))
altura=float(input('Digite sua altura: '))
imc=peso/altura**2

print('Ok seu peso é {} e sua altura é {}, e o cáculo do IMC {:.2f}'.format(peso,altura,imc))

if imc<18.5:
    print('Está abaixo do peso')
elif imc>=18.5 and imc<=25:
    print('Está no peso ideal')
elif imc>=25 and imc<=30:
    print('Está em sobrepeso')
elif imc>=30 and imc<=40:
    print('Está entre a Obsidade')
elif imc>40:
    print('Cuidado! você está acima do peso')
