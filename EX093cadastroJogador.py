player = {}
player['playerName'] = str(input('Nome do jogador? '))
matches = int(input(f'Quantas partidas {player["playerName"]} jogou? '))
player['playerGoals'] = []
for c in range(1, matches+1):
    player['playerGoals'].append(int(input(f'    Quantos gols na {c}ª partida? ')))
player['total'] = sum(player['playerGoals'])
print('-='*50)
print(player)
print('-='*50)
for k, v in player.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*50)
print(f'O jogador {player["playerName"]} jogou {matches} partidas.')
for i, v in enumerate(player['playerGoals']):
    print(f'==> Na partida {i+1}, fez {v} gols.')
