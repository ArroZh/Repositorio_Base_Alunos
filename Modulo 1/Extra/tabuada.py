try:
    numero = int(input("Digite um numero: "))
    contador = 1

    while contador <= 10:
     print(numero * contador)
     contador = contador + 1

except ValueError:
   print("Apenas números inteiros!")