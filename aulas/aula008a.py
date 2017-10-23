from math import sqrt, floor
import random

num = int(input('Digite um numero: '))
raiz = sqrt(num)

print('A raiz quadrada de {} é {}'.format(num, floor(raiz)))

n1 = random.random()
n2 = random.randint(1, 30)
print(n1)
print(n2)
