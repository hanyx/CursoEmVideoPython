sal = float(input('Digite seu salario: '))

if (sal > 1250):
    print('Salario com aumento de 10%: R${:.2f}'.format(sal*1.1))
else:
    print('Salario com aumento de 15%: R${:.2f}'.format(sal * 1.15))
