print('\033[1:30:44m CALCULADORA DE IMC ')
weight = float(input('Qual é o seu peso (KG): '))
height = float(input('Qual é a sua altura (METROS): '))
imc = weight/(height**2)
if imc <= 18.5:
    print('\033[1:30:47m Seu imc é {:.1f}, você está abaixo do peso.'.format(imc))
elif imc <= 25:
    print('\033[1:30:42m Seu imc é {:.1f}, você está na faixa de peso ideal. continue assim'.format(imc))
elif imc <= 30:
    print('\033[1:30:43m Seu imc é {:.1f}, você está acima do peso.'.format(imc))
elif imc <= 40:
    print('\033[1:30:41m Seu imc é {:.1f}, você está com obesidade grau I. procure um médico'.format(imc))
else:
    print('\033[1:30:41m Seu imc é {:.1f}, você está com obesidade grau II. procure um médico'.format(imc))
print('\033[1:30:44m Até mais!!')

