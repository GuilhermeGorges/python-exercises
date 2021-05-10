from random import randint
from time import sleep
print('-'*40)
print(f"{'PALPITES DA MEGA SENA':^40}")
print('-'*40)
sortNum = int(input('Quantos jogos você quer que eu sorteie? '))
print('-=' *3, f'SORTEANDO {sortNum} JOGOS', '=-' *3)
for c in range(0, sortNum):
    lista = list()
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont == 6:
            break
    print(f'Jogo {c + 1}: {lista}')
    sleep(1)
print('-=' *3, f'< BOA SORTE! >', '=-' *3)

