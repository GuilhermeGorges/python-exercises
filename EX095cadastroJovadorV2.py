players = []
while True:
    player = {}
    player['playerName'] = str(input('Nome do jogador? '))
    matches = int(input(f'Quantas partidas {player["playerName"]} jogou? '))
    player['playerGoals'] = []
    for c in range(1, matches+1):
        player['playerGoals'].append(int(input(f'    Quantos gols na {c}ª partida? ')))
    player['total'] = sum(player['playerGoals'])
    players.append(player)
    while True:
        again = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if again in 'SN':
            break
        print('ERROR! Answer only S or N!')
    if again in 'N':
        break
print('-='*50)
print(f'{"Cod":>}{"Name":>5}{"Goals":>20}{"Total":>18}')
print(f'--'*24)
for k, v in enumerate(players):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f"{str(d):<19}", end='')
    print()
while True:
    print(f'--' * 24)
    whichPlayer = int(input('Mostar dados de qual jogador? [999 to EXIT] '))
    if whichPlayer == 999:
        print('<<< PROGRAMA ENCERRADO >>>')
        break
    if whichPlayer >= len(players):
        print('ERROR! Jogador inexistente tente novamente...')
    else:
        print(f'-- Levantamento do jogador {players[whichPlayer]["playerName"]} que jogou {len(players[whichPlayer]["playerGoals"])} partidas.')
        for i, v in enumerate(players[whichPlayer]["playerGoals"]):
            print(f'    ==> Na partida {i + 1}, fez {v} gols.')
print('<<   VOLTE SEMPRE !!   >>')
