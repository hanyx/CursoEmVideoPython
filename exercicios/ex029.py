vel = int(input('Qual a velocidade do carro? '))

if vel > 80:
    print('Voce foi multado em: R${:.2f}'.format(7*(vel-80)))
