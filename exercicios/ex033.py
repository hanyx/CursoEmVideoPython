n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
n3 = int(input('Digite um numero: '))

if n1 > n2 and n1 > n3:
    print('O maior numero é {}'.format(n1))
if n2 > n1 and n2 > n3:
    print('O maior numero é {}'.format(n2))
if n3 > n2 and n3 > n1:
    print('O maior numero é {}'.format(n3))

if n1 < n2 and n1 < n3:
    print('O menor numero é {}'.format(n1))
if n2 < n1 and n2 < n3:
    print('O menor numero é {}'.format(n2))
if n3 < n2 and n3 < n1:
    print('O menor numero é {}'.format(n3))