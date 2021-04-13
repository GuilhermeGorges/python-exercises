num = int(input('Digite um numero para calcular o fatorial: '))
c = num
f = 1
print('Calculando {}! = '.format(num), end='')
while c > 0:
    print('{} '.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))

""""SOLUÇÃO COM FOR 
num = int(input('Digite um numero para calcular o fatorial: '))
c = num
f = 1
print('Calculando {}! = '.format(num), end='')
for fat in range(num, 0, -1):
    print('{} '.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))"""