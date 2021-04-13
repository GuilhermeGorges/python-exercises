from random import randint
sorteio = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
print(f'Os valores sorteados foram: ', end='')
for n in sorteio:
    print(f'{n} ', end='')
print(f'O maior valor sorteado foi {max(sorteio)}')
print(f'O menor valor sorteado foi {min(sorteio)}')
