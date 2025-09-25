try:
    numero_1 = int(input("Digite o primeiro numero: "))
    numero_2 = int(input("Digite o segundo numero: "))
    resultado = numero_1 + numero_2

    print(f"A soma dos numeros é: {resultado} ")


except ValueError:
    print("Somente permitido números inteiros.")

