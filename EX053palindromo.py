from time import  sleep
frase = str(input('\033[2:30:44m Digite uma fraze: ')).upper()
print('PROCESSANDO FRASE')
sleep(2)
fraseSemEspaco = list(''.join(frase.split()))
fraseReverse = []
for reverse in fraseSemEspaco[::-1]:
    fraseReverse.append(reverse)

if fraseSemEspaco == fraseReverse:
    print('A frase {} é um PALÍNDROMO.'.format(frase, fraseReverse))
else:
    print('A frase {} não é um PALÍNDROMO'.format(frase, fraseReverse))


"""Resolução Guanabara
inverso = ''
for letra in range(len(fraseSemEspaco) -1, -1, -1):
    inverso += fraseSemEspaco[letra]
if inverso == fraseSemEspaco:
    print('temos um palíndromo!')
else:
    print('Não temos um palindromo!')

ou 

fraseReverse = [::-1]"""

