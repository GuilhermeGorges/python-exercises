from random import randint
from time import sleep
itens = ('PEDRA' , 'PAPEL' , 'TESOURA')
machine = randint(0, 2)
print('\033[1:30:46m JOGO DE PEDRA - PAPEL - TESOURA')
sleep(1)
print('ESCOLHA UMA DAS OPÇÕES:')
print('[0] PARA PEDRA \n[1] PARA PAPEL \n[2] PARA TESOURA')
sleep(2)
human = int(input('DIGITE SUA ESCOLHA => '))
print('-----------JO----------')
sleep(1)
print('-----------KEN---------')
sleep(1)
print('-----------PO----------')
print('-=-'*10)
print('VOCÊ ESCOLHEU {}.'.format(itens[human]))
print('EU ESCOLHI {}'.format(itens[machine]))
print('-=-'*10)
sleep(3)
if machine == 0: #PC JOGOU PEDRA
    if human == 0:
        print('NOS EMPATAMOS!!')
    elif human == 1:
        print('VOCÊ ME VENCEU PARABÉNS!!')
    elif human == 2:
        print('VOCÊ PERDEU E EU VENCI, A MAQUINA SEMPRE VENCE!!')
    else:
        print('JOGADA INVÁLIDA')
elif machine == 1: #PC JOGOU PAPEL
    if human == 0:
        print('VOCÊ PERDEU E EU VENCI, A MAQUINA SEMPRE VENCE!!')
    elif human == 1:
        print('NOS EMPATAMOS!!')
    elif human == 2:
        print('VOCÊ ME VENCEU PARABÉNS!!')
    else:
        print('JOGADA INVÁLIDA')
elif machine == 2: #PC JOGOU TESOURA
    if human == 0:
        print('VOCÊ ME VENCEU PARABÉNS!!')
    elif human == 1:
        print('VOCÊ PERDEU E EU VENCI, A MAQUINA SEMPRE VENCE!!')
    elif human == 2:
        print('NOS EMPATAMOS!!')
    else:
        print('JOGADA INVÁLIDA')
print('-=-'*10)
sleep(2)
print('VAMOS NOVAMENTE?')