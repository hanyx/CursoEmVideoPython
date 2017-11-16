frase = str(input('Digite uma frase: ')).strip().upper()
separado = frase.split(' ')
junto = ''.join(separado)
invertido = ''

for let in range(len(junto)-1, -1, -1):
    invertido += junto[let]

print('{} ao contrário é {}'.format(junto, invertido))

if junto == invertido:
    print('Logo, é um palíndromo')
else:
    print('Logo, não é um palíndromo')
