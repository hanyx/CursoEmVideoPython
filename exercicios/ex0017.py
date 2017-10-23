import math

catOp = float(input('Digite o cateto oposto: '))
catAd = float(input('Digite o cateto adjacente: '))

#hip = math.sqrt(pow(catOp, 2) + pow(catAd, 2))
hip2 = math.hypot(catAd, catOp)

#print('A hipotenusa é: {:.3f}'.format(hip))
print('A hipotenusa é: {:.3f}'.format(hip2))
