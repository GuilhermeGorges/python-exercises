print('-=-'*30)
print('Sequência de Fibonatti')
print('-=-'*30)
num = int(input('Quantos termos você quer mostrar? '))
fibo = [0]
contador = 0
while contador < num+1:
    if contador < 1:
        fibo.append(0+1)
    elif contador < num:
        fibo.append(fibo[-1]+fibo[-2])
    else:
        print('Esta é a sequencia de fibonatti até o {} termo da sequência = {}'.format(num, fibo))
        numcont = int(input('Você deseja continuar? se sim digite o Nº de vezes se não digite [0] '))
        num = num + numcont
    contador += 1
print('END')

"""GUANABARA
t1 = 0
t2 = 1
print('{} > {}'.format(t1, t2), end='')
cont = 3
while cont <= num:
    t3 = t1 + t2
    print('{} > {}'.format(t1, t2), end='')
    t1 = t2
    t2 = t3
    cont += 1
"""