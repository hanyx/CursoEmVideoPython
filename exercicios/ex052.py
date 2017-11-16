n = int(input('Digite um numero: '))
flag = True

for i in range(2, n):
    if (n % i == 0):
        flag = False
        break

if flag:
    print('{} é primo'.format(n))
else:
    print('{} não é primo'.format(n))
