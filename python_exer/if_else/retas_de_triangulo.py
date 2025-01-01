print('Digite até três números para saber se forma um triângulo ou não')
reta1=int(input('Digite a primeira reta: '))
reta2=int(input('Digite a segunda reta: '))
reta3=int(input('Digite a terceira reta: '))

if reta1 == reta2 + reta3 or reta2 == reta1 + reta3:
    print('PARABÉNS! Você formou um isósceles, pode forma um triângulo')
    
elif reta3 > reta1 + reta2 or reta3 > reta2 + reta1:
    print('É um isósceles mas não foi formado um triângulo')

elif reta1 != reta2 + reta3 or reta2 != reta1 + reta3:
    print('PARABÉNS! Você formou um escaleno, pode forma um triângulo')

elif reta3 > reta1+reta2 and reta1 != reta2 or reta3 > reta2 + reta1 and reta2 != reta1:
    print('É um escaleno mas não foi formado um triângulo')

elif reta1 == reta2 == reta3 and reta1 + reta2 > reta3:
    print("PARABÉNS! Você formou um equilátero, e forma um triângulo")

elif reta3 > reta1 == reta2 and reta3 > reta1 +reta2:
    print('É um equilátero, mas não form um triângulo')

print("--FIM--")
