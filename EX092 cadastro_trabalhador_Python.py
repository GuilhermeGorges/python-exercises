from datetime import date
profile = {}
profile['name'] = str(input('Nome: '))
bornAge = int(input('Ano de Nascimento: '))
profile['age'] = date.today().year - bornAge
jobWalletNumber = int(input('Carteira de Trabalho (0 não tem): '))
profile['jobWalletNumber'] = jobWalletNumber
if jobWalletNumber != 0:
    profile['hiring'] = int(input('Ano de contratação: '))
    profile['salary'] = int(input('Salário: R$ '))
    profile['retirement'] = profile['age'] + ((profile['hiring'] + 35) - date.today().year)
for k, v in profile.items():
    print(f'O {k} é {v}')