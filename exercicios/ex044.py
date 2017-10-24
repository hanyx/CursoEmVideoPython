preco = float(input('Valor do produto: '))
print('Qual a forma de pagamento?')
print("""1 - A vista no dinheiro ou cheque
2 - A vista no cartão
3 - Até 2x no cartão
4 - 3x ou mais no cartão""")
op = int(input('Sua opção: '))

if op == 1:
    print('Preço final: R${:.2f}'.format(0.9*preco))
elif op == 2:
    print('Preço final: R${:.2f}'.format(0.95 * preco))
elif op == 3:
    print('Preço final: R${:.2f}'.format(preco))
else:
    print('Preço final: R${:.2f}'.format(1.2 * preco))
