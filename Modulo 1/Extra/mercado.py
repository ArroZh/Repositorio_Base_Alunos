import time

def print_lento(texto,delay=0.03):
    for char in str(texto):
        print(char,end='',flush=True)
        time.sleep(delay)

print("---------------------------------------------------")
print_lento("Seja bem vindo, aproveite a promoção!\n")

nome = input("Digite o nome do produto: ")
valor = input("Digite o valor do produto: ")
quantidade = input("Digite a quantidade do produto: ")


with open ("americanas.txt", "a") as arquivo:
    arquivo.write(f"{nome} | {valor} | {quantidade}\n")


print_lento("Volte sempre!")
print("---------------------------------------------------")