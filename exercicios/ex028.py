import random

pc = random.randint(0, 5)
user = int(input('Digite um numero entre 0 e 5: '))

if pc == user:
    print('Você acertou')
else:
    print('Você errou')
