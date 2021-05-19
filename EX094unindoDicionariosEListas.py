people = []
peopleAge = count = peopleAgeAverage = 0
women = []
while True:
    person = {}
    person['name'] = str(input('Nome: '))
    while True:
        person['gender'] = str(input('Sexo: M ou F ')).strip().upper()[0]
        if person['gender'] in 'MF':
            break
        print('ERROR! Please, digit only M or F!')
    person['age'] = int(input('Idade: '))
    peopleAge += person['age']
    people.append(person)
    while True:
        more = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if more in 'SN':
            break
        print('ERROR! Answer only S or N!')
    if more == 'N':
        break
print('-='*50)
print(f'A - Ao todo temos {len(people)} pessoas cadastradas.')
peopleAgeAverage = peopleAge / len(people)
print(f'B - A média de idade é de {peopleAgeAverage:5.2f} anos.')
for c in people:
    if people[count]['gender'] == 'F':
        women.append(people[count]['name'])
    count += 1
print(f'C - As mulheres cadastradas foram: {women}')
print(f'D - Lista das pessoas que estão acima da média: ')
print()
count = 0
for c in people:
    if people[count]['age'] >= peopleAgeAverage:
        print(f'      Nome = {people[count]["name"]}; Sexo = {people[count]["gender"]}; Idade = {people[count]["age"]};')
    count += 1
print("<<END>>")