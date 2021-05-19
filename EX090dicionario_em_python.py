aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Media'] = float(input('Média: '))
if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')