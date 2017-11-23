v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))

opcao = 0
while opcao != 5:
    print("""\n------ MENU ------
             1 - SOMAR
             2 - MUTIPLICAR
             3 - MAIOR
             4 - NOVOS NUMEROS
             5 - SAIR

          """)
    opcao = int(input("O que você deseja: "))
    print("\n")
    if (opcao == 1):
        print("{} + {} = {}".format(v1, v2, v1 + v2))
    elif (opcao == 2):
        print("{} X {} = {}".format(v1, v2, v1 * v2))
    elif (opcao == 3):
        print("O maior é {}".format(max(v1, v2)))
    elif (opcao == 4):
        v1 = int(input("Digite o primeiro valor: "))
        v2 = int(input("Digite o segundo valor: "))
    elif (opcao == 5):
        print("Até mais!")
    else:
        print("Opção Inválida")
