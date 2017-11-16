from datetime import date
maiores = menores = 0
atual = date.today().year

for i in range(0, 7):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(i+1)))
    if (atual - ano >= 21):
        maiores += 1
    else:
        menores += 1

print('São {} pessoas maiores de idade e {} menores de idade'.format(maiores, menores))
