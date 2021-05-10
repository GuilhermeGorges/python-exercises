matriz = [[], [], []]
count = pairSum = 0
for l in range(0, 3):
    for c in range(0, 3):
        num = (int(input(f'Digite um valor para [{l}, {c}]: ')))
        matriz[l].append(num)
        if num%2 == 0:
            pairSum += num
for c in range(0, 3):
    print(f'[{matriz[c][0]:^5}][{matriz[c][1]:^5}][{matriz[c][2]:^5}]')
print('-='*30)
print(f'A soma dos valores pares é {pairSum}')
print(f'A soma dos valores da terceira coluna é {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')
