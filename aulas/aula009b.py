frase = 'Curso em video python'

print(len(frase))
print(frase.count('o'))
print(frase.count('o', 0, 13))
print(frase.find('deo'))
print(frase.find('android'))
print('Curso' in frase)
print(frase.replace('python', 'android'))
print(frase.upper())
print(frase.capitalize())
print(frase.title())
print(frase.split(' '))
print('-'.join(frase.split()))
