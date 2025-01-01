num=0
while num != -1:
    num=int(input('Diga o número[-1 para parar]: '))
    if num == -1:
        break
    print('{}+{} = {}'.format(num, 1, num+1))
    print('{}+{} = {}'.format(num, 2, num+2))
    print('{}+{} = {}'.format(num, 3, num+3))
    print('{}+{} = {}'.format(num, 4, num+4))
    print('{}+{} = {}'.format(num, 6, num+6))
    print('{}+{} = {}'.format(num, 7, num+7))
    print('{}+{} = {}'.format(num, 8, num+8))
    print('{}+{} = {}'.format(num, 9, num+9))
    print('{}+{} = {}'.format(num, 10, num+10))

    print('**'*40)
    print('{}x{} = {}'.format(num, 1, num*1))
    print('{}x{} = {}'.format(num, 2, num*2))
    print('{}x{} = {}'.format(num, 3, num*3))
    print('{}x{} = {}'.format(num, 4, num*4))
    print('{}x{} = {}'.format(num, 6, num*6))
    print('{}x{} = {}'.format(num, 7, num*7))
    print('{}x{} = {}'.format(num, 8, num*8))
    print('{}x{} = {}'.format(num, 9, num*9))
    print('{}x{} = {}'.format(num, 10, num*10))
    
    print('**'*40)
    
    print('{}-{} = {}'.format(num, 1, num-1))
    print('{}-{} = {}'.format(num, 2, num-2))
    print('{}-{} = {}'.format(num, 3, num-3))
    print('{}-{} = {}'.format(num, 4, num-4))
    print('{}-{} = {}'.format(num, 6, num-6))
    print('{}-{} = {}'.format(num, 7, num-7))
    print('{}-{} = {}'.format(num, 8, num-8))
    print('{}-{} = {}'.format(num, 9, num-9))
    print('{}-{} = {}'.format(num, 10, num-10))

print('**FIM**')
