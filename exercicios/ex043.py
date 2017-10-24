altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em kg: '))

imc = peso / altura**2

print('Seu IMC é {}, você está '.format(imc), end='')
if imc < 18.5:
    print('abaixo do peso')
elif imc < 25:
    print('com peso ideal')
elif imc < 30:
    print('com sobrepeso')
elif imc < 40:
    print('com obesidade')
else:
    print('com obesidade mórbida')
