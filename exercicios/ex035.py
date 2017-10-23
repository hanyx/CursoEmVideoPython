r1 = int(input('Digite o comprimento de uma reta: '))
r2 = int(input('Digite o comprimento de uma reta: '))
r3 = int(input('Digite o comprimento de uma reta: '))

if (r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2):
    print('É possivel formar um triangulo com as retas dadas.')
else:
    print('É impossivel formar um triangulo com as retas dadas.')
