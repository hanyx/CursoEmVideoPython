nome = str(input('Digite seu nome: ')).strip()

#print('Voce tem Silva no nome: {}'.format(nome.lower().count('silva') != 0))
print('Voce tem Silva no nome: {}'.format('silva' in nome.lower()))
