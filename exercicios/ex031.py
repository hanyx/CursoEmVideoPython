dist = int(input('Qual a distancia da viagem? '))

if dist <= 200:
    preco = 0.5*dist
else:
    preco = 0.45*dist
print('Sua passagem vai custar R${:.2f}'.format(preco))
