from random import randint
from time import sleep
print("\033[1:31:31m-=-"*20)
print('Estou pensando em um numero de 0 á 5........')
print("-=-"*20)
human = int(input('Em qual número estou pensando??? '))
print("-=-"*20)
print('Processando...')
sleep(1)
machine = randint(0, 5)
contador = 1
while human != machine:
    print("-=-" * 20)
    human = int(input('Errou Tente novamente!!! ~~~> '))
    print("-=-" * 20)
    print('Processando...')
    print("-=-" * 20)
    sleep(1)
    machine = randint(0, 5)
    contador += 1
print('Parabéns após {} tentativas, você adivinhou o numero que eu estava pensando que é {}.'.format(contador, machine))
print("-=-" * 20)
