from random import randint
from time import sleep
print('\033[1:34m-=-'*30)
print('LETS PLAY ODDS OR EVENS')
print('-=-'*30)
won = 0
while True:
    humannum = int(input('TYPE A NUMBER: '))
    humanchoise = str(input('ODD OR EVENS? [O/E] ').upper().strip()[0])
    while humanchoise not in 'OoEe':
        humanchoise = str(input('ODD OR EVENS? [O/E] ').upper().strip()[0])
    machine = randint(1, 10)
    somahm = humannum + machine
    isparimp = somahm%2
    print('-=-' * 30)
    print('-----ONE-----')
    print('-=-' * 30)
    sleep(1)
    print('-----TWO-----')
    print('-=-' * 30)
    sleep(1)
    print('-----THREE-----')
    print('-=-' * 30)
    sleep(1)
    print(f'You played {humannum} and the computer played {machine}. Total {somahm}. ', '---IS ODD---' if isparimp == 0 else '---IS EVEN---')

    if humanchoise == 'O':
        if isparimp == 0:
           won += 1
        else:
            print('-=-' * 30)
            print('YOU LOSE!')
            break
    else:
        if isparimp != 0:
            won += 1
        else:
            print('-=-' * 30)
            print('YOU LOSE!')
            break
    print('-=-' * 30)
    print('You Win!')
    print('Lets Play Again..')
    print('-=-' * 30)

print('-=-' * 30)
print(f'GAME OVER! YOU WON {won} TIMES.')

