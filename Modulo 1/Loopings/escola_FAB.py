numero = int(input("Digite um numero: "))
inicio = int(input("Digite da onde vai começar: "))
final = int(input("Digite onde vai terminar: "))

for i in range(inicio, final+1):

    print(f"{i} x {numero} = {i * numero}")
