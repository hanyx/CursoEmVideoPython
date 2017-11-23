sexo = ""

while sexo != "M" and sexo != "F":
    sexo = str(input("Digite seu sexo(M ou F): ")).upper()

if sexo == "M":
    print ("Sexo Masculino!")
else:
    print ("Sexo Feminino!")
