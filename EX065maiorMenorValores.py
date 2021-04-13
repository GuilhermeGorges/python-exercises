num = int(input('Digite um numero: '))
numeros = [num]
while num != 0:
    num = int(input('Digite outro número: [0] = SAIR  '))
    if num == 0:
        print('Fim')
    else:
        numeros.append(num)
print('Os {} números digitados foram -> {}'.format(len(numeros), numeros))
print('A média dos números digitados é de -> {}.'.format(sum(numeros)/len(numeros)))
print('O maior número digitado foi -> {}.'.format(max(numeros)))
print('O menor número dígitado foi -> {}.'.format(min(numeros)))
print('A soma dos números digitados é de -> {}. '.format(sum(numeros)))
