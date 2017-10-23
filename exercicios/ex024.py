cidade = str(input('Digite o nome de uma cidade: ')).strip()

print('O nome da cidade começa com SANTO: {}'.format(cidade.split(' ')[0].lower() == 'santo'))
