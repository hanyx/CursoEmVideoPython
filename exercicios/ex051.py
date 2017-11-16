primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

print('Os 10 primeiros termos da PA são:')

for i in range(0, 10):
    print('{}'.format(primeiro + i*razao), end=' -> ')
print('END')
