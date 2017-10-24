v1 = int(input('Digite um valor: '))
v2 = int(input('Digite um valor: '))
v3 = int(input('Digite um valor: '))

if v1 < v2+v3 and v2 < v1+v3 and v3 < v1+v2:
    if v1 == v2 and v2 == v3:
        print('É possível formar um triangulo equilátero!')
    elif v1 == v2 or v1 == v3 or v2 == v3:
        print('É possível formar um triango isósceles')
    else:
        print('É possível formar um triangulo escaleno')
else:
    print('É impossível formar um triangulo!')
