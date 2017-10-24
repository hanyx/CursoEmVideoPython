from random import choice
from time import sleep

lista = ['Pedra', 'Papel', 'Tesoura']
pc = choice(lista)
jogador = str(input('Pedra, Papel ou Tesoura??? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')

if jogador.lower() == 'pedra':
    if (pc == 'Pedra'):
        print('Pedra com pedra, empate!!!')
    elif (pc == 'Papel'):
        print('Papel engole pedra, venci!!!')
    else:
        print('Pedra quebra tesoura, você venceu :(')
elif jogador.lower() == 'tesoura':
    if (pc == 'Pedra'):
        print('Pedra quebra tesoura, venci!!')
    elif (pc == 'Papel'):
        print('Tesoura corta papel, você venceu :(')
    else:
        print('Tesoura com tesoura, empate!!!')
else:
    if (pc == 'Pedra'):
        print('Papel engole pedra, você venceu :(')
    elif (pc == 'Papel'):
        print('Papel com papel, empate!!!')
    else:
        print('Tesoura corta papel, venci!!!')
