nome = str(input('Digite seu nome completo: '))

print('O nome com todas as letras maiúsculas é: {}'.format(nome.upper()))
print('O nome com todas as letras minúsculas é: {}'.format(nome.lower()))
print('O nome tem ao total {} letras, sem considerar espaços'.format(nome.__len__() - nome.count(' ')))
print('O primeiro nome tem {} letras'.format(nome.split()[0].__len__()))
