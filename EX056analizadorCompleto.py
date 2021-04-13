#listas dos dados
nomesMulheres = []
idadesMulheres = []
mulheresMenores = []
nomesHomens = []
idadesHomens = []
#laço para captura dos dados
numConsultar = int(input('Digite o numero de pessoas que você pretende consultar: '))
for person in range(0, numConsultar):
    print('---- {}ª PESSOA ----'.format(person+1))
    sexo = int(input('SEXO: [1] para MULHER [2] para HOMEM '))
    if sexo == 1:
        nomesMulheres.append(str(input('NOME: ')))
        idadeMulher = int(input('IDADE: '))
        idadesMulheres.append(idadeMulher)
        if idadeMulher < 20:
            mulheresMenores.append(idadeMulher)
    elif sexo == 2:
        nomesHomens.append(str(input('NOME: ')))
        idadesHomens.append(int(input('IDADE ')))
    else:
        print('ERROR OPÇÃO INEXISTENTE')
        numConsultar = person
        break

#tratamento dos dados (media idade)
idadeMedia = sum(idadesMulheres + idadesHomens)/numConsultar
print('A idade média dos {} participantes da pesquisa é de {:.0f} anos. '.format(numConsultar, idadeMedia))

#tratamento dos dados (homem mais velho)
idadeHomemMaisVelho = max(idadesHomens, key=int)
homemMaisVelho = idadesHomens.index(idadeHomemMaisVelho)
print('O nome do homem mais velho se chama {} e tem {} anos.'.format(nomesHomens[homemMaisVelho], idadeHomemMaisVelho))

#tratamento dos dados (mulheres <20

print('Dos dados recebidos {} mulheres tem menos de 20 anos.'.format(len(mulheresMenores)))

