from random import randint
from time import sleep
from operator import itemgetter
jogadores = {}
ranking = []
for c in range(1, 5):
    result = randint(1, 6)
    jogadores[f'jogador{c}'] = result
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True) #comando para colocar em sequencia
print('Valores Sorteados:')
for k, v in jogadores.items():
    print(f'O {k} tirou {v} ')
    sleep(1)
print('-='* 30)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)