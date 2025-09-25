import math 
import random
import time

def print_lento(texto,delay=0.03):
    for char in str(texto):
        print(char,end='',flush=True)
        time.sleep(delay)
    print()
nomes = ["Diego", "Tânia", "Vanessa" , "Samuel" , "Levi" , "Joaquim"]

print_lento(len(nomes))



del nomes[random.randint(0,len(nomes) - 1)]

print_lento(nomes)
input("Aperte enter para continuar")


del nomes[random.randint(0,len(nomes) - 1)]

print_lento(nomes)

input("Aperte enter para continuar")



del nomes[random.randint(0,len(nomes) - 1)]

print_lento(nomes)

input("Aperte enter para continuar")


del nomes[random.randint(0,len(nomes) - 1)]

print_lento(nomes)
input("Aperte enter para continuar")



del nomes[random.randint(0,len(nomes) - 1)]


print_lento(f"O nome final é: {nomes}")




