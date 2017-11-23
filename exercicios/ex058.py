from random import randint
from time import sleep

print("Vou escolher um numero entre 1 e 10, você consegue advinhar???")
print("Deixe-me escolher...\n")
computador = randint(1, 10)
sleep(1)
print("Pronto! Quantas tentativas voce precisa para advinhar?\n")
tent = 1
user = int(input("Digite sua escolha: "))

while user != computador:
    tent += 1
    print("Você errou!!! Tente novamente!")
    user = int(input("Digite sua escolha: "))

print("\nVocê me descobriu com {} tentativas!!!".format(tent))
