nome = str(input('Digite seu nome completo: ')).strip()

print('Seu primeiro nome: {}'.format(nome.split()[0]))
print('Seu ultimo nome: {}'.format(nome.split()[nome.split().__len__()-1]))
