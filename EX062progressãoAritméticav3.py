print('GERADOR DE PA')
print('-='*30)
primeiroTermo = int(input("Primeiro Termo da PA: "))
razaoPa = int(input("Razão da PA: "))
fim = 10
repetidor = primeiroTermo
contador = 1
while contador <= fim:
    print('{} > '.format(repetidor), end='')
    repetidor += razaoPa
    contador += 1
    if contador == fim+1:
        print('PAUSA')
        print('Você quer continuar? ')
        maisx = int(input('Se sim digite o nº de X, se não digite [0]:  '))
        fim += maisx
print('END')
