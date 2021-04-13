valorProd = float(input('\033[1:30:45m DIGITE O VALOR DO PRODUTO: '))
print('FORMAS DE PAGAMENTO: '
      '[0] Á VISTA (DINHEIRO OU CHEQUE) '
      '[1] A VISTA (CARTÃO) '
      '[2] 2X NO CARTÃO '
      '[3] 3X NO CARTÃO OU MAIS ')
formaPag = int(input('DIGITE A FORMA DE PAGAMENTO: '))
if formaPag == 0:
    valorFinal = valorProd - (valorProd*0.10)
    print('\033[1:30:45m O valor a ser pago pelo produto é de R$ {:.1f}'.format(valorFinal))
elif formaPag == 1:
    valorFinal = valorProd - (valorProd*0.05)
    print('\033[1:30:45m O valor a ser pago pelo produto é de R$ {:.1f}'.format(valorFinal))
elif formaPag == 2:
    valorFinal = valorProd
    valorDaParcela = valorFinal / 2
    print('\033[1:30:45m O valor a ser pago pelo produto é de R$ {:.1f} em 2 parcelas de R$ {} no cartão.'.format(valorFinal, valorDaParcela))
elif formaPag == 3:
    valorFinal = valorProd * 1.20
    parcelas = int(input('\033[1:30:45mDIGITE O NUMERO DE PARCELAS: '))
    valorDaParcela = valorFinal / parcelas
    print('\033[1:30:45m O valor total a ser pago pelo produto é de R$ {:.1f} em {} parcelas de R$ {} no cartão.'.format(valorFinal, parcelas, valorDaParcela))
else:
    print('\033[1:30:42m ERROR! Opção Inválida.')
print('\033[1:30:45m Muito Obrigado. Volte Sempre!!!')