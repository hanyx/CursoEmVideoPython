maior = menor = float(input('Digite o peso da 1ª pessoa: '))

for i in range (2, 6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(i)))
    if peso < menor:
        menor = peso
    if peso > maior:
        maior = peso

print('A pessoa mais pesada tem {}kg e a mais leve tem {}kg'.format(maior, menor))
