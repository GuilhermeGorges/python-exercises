inteiro = int(input('Digite um numero inteiro: '))
tot = 0
for primo in range(1, inteiro + 1):
    if inteiro % primo == 0:
        print('\033[34m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(primo), end= '')
print('\n\033[mO número {} foi divisivel {} vezes'.format(inteiro, tot))
if tot == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele não é primo')

