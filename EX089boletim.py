students = []
while True:
    nome = (str(input('Nome: ')))
    note1 =(float(input('Nota 1: ')))
    note2 = (float(input('Nota 2: ')))
    media = (note1 + note2) / 2
    students.append([nome, [note1, note2], media])
    again = input(str('Quer continuar [S/N] ')).strip().upper()
    while again not in 'SN':
        again = input(str('Quer continuar [S/N] ')).strip().upper()
    if again == 'N':
        break
print('-='*20)
print(f'{"No.":<4}{"NOME":<10}{"Média":>25}')
print('-'*40)
for c, v in enumerate(students):
    print(f'{c:<4}{students[c][0]:<10}{students[c][2]:>25}')

while True:
    print('-'*40)
    id = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if id == 999:
        break
    if id < len(students):
        print(f'Notas de {students[id][0]} são {students[id][1]}')
    else:
        print('Aluno inexistente')
print('<<< Volte Sempre >>>')