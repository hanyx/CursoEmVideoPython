somaIdades = 0
idadeHomemVelho = 0
nomeHomemVelho = ''
mulheresMenos20 = 0

for i in range(1, 5):
    print('=========={}ª PESSOA========='.format(i))
    nome = str(input('Digite seu nome: ')).strip()
    sexo = str(input('Digite seu gênero: ')).strip()
    idade = int(input('Digite sua idade: '))
    somaIdades += idade
    if sexo.upper()[0] == 'M' and idade > idadeHomemVelho:
        idadeHomemVelho = idade
        nomeHomemVelho = nome
    if sexo.upper()[0] == 'F' and idade < 20:
        mulheresMenos20 += 1

mediaIdades = float(somaIdades / 4.0)

print('A media das idades é {} anos\nO homem mais velho se chama {}\nExistem {} mulheres com menos de 20 anos'.format(mediaIdades, nomeHomemVelho, mulheresMenos20))
