valores = []
pares = []
impares = []
while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    """if valor >= 0: #Solução mais simples 
        if valor%2 == 0:
            pares.append(valor)
        else:
            impares.append(valor)"""
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == "N":
        break
for v in valores: #como o guanabara pediu
    if v >= 0:
        if v%2 == 0:
            pares.append(v)
        else:
            impares.append(v)
print('-=-'*30)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impares}')
