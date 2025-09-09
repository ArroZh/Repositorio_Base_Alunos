import random

print("SUPER JOGO DE ADIVINHAÇÂO DO NÚMERO MÁGICO.")
numero_magico = random.randint(1,100)
numero_adivinhacao = int(input("Digite um número entre 1 e 100: "))
tentativas = 0

while numero_adivinhacao != numero_magico:

    if numero_adivinhacao > numero_magico:
        print("O número é menor.")

    else:
        print("o número é maior.")

    tentativas += 1
    numero_adivinhacao = int(input("Tente novamente: "))

print(f"Parabéns, você acertou em {tentativas} tentativas!")