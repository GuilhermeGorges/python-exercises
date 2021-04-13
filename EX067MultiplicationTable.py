while True:
    count = 1
    tabu = int(input('Digite um número para saber a tabuada --> '))
    if tabu < 0:
        print('PROGRAMA DE TABUADA ENCERRADO. VOLTE SEMPRE!')
        break
    print('-=-'*30)
    while count <= 10:
        print(f'{tabu} x {count} = {tabu*count}')
        count += 1
    print('-=-'*30)