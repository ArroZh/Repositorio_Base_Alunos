
nome = input("Digite seu nome: ")
peso = float(input(" Digite seu peso: "))
altura = float (input(" Digite sua altura: "))

imc = peso / (altura * altura)

if imc <= 18.5:
    situacao = "Abaixo do peso."
elif imc <= 24.9:
    situacao = "Peso normal."
elif imc <= 29.9:
    situacao = "Sobrepeso."
elif imc <= 30:
    situacao = "Cuidado com a saúde!"
elif imc <= 34.9:
    situacao = "Obesidade Grau I"
elif imc <= 39.9:
    situacao = "Obesidade Grau II"
else:
   situacao = "Obesidade de grau III, mórbida"

print(f"{situacao}")

with open ("imc.txt", "a") as arquivo:
    arquivo.write(f"{nome} | {imc} | {situacao}\n")