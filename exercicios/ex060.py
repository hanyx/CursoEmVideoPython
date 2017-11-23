num = int(input("Digite um numero: "))
n = num
fat = num

while num > 1:
    num -= 1
    fat *= num

print("{}! = {}".format(n, fat))
