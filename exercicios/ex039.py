from datetime import date

nasc = int(input('Digite seu ano de nascimento: '))
ano = date.today().year

idade = ano - nasc

if idade < 18:
    print('Voce ainda terá de se alistar')
elif idade == 18:
    print('Voce está na idade de se alistar')
else:
    print('Você já deveria ter se alistado')
