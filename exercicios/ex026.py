frase = str(input('Digite uma frase: ')).strip()

print('Sua frase tem {} letra(s) A'.format(frase.lower().count('a')))
print('A primeira letra A aparece na {}ª posição'.format(frase.lower().find('a')))
print('A ultima letra A aparece na {}ª posição'.format(frase.lower().rfind('a')))
