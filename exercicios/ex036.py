valor = float(input('Qual o valor da casa? R$'))
sal = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos pretende pagar? '))

parcela = valor / (anos*12)

if parcela <= 0.3*sal:
    print('Seu empréstimo foi aprovado! A parcela irá custar R${:.2f}'.format(parcela))
else:
    print('Seu empréstimo não foi aprovado!')
