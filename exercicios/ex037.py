numero = int(input('Digite um numero: '))
print('Para qual base você deseja converter?')
print('1 - Binário\n2 - Octal\n3 - Hexadecimal')
base = int(input('Sua escolha: '))

if base == 1:
    print('{} em binário é igual a {}'.format(numero, bin(numero)[2:]))
elif base == 2:
    print('{} em octal é igual a {}'.format(numero, oct(numero)[2:]))
else:
    print('{} em hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))
