print("P.A")
a1 = int(input('Digite o primeiro termo: '))
r =  int(input('Digite a razão: '))
for a1 in range(0,10):
    t = a1 + r
    t += t
    print(t, end=' ')

