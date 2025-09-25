try:
    peso = float(input(" Digite seu peso: "))
    altura = float (input(" Digite sua altura: "))

    imc = peso / (altura * altura)

    print(f"seu imc é: {imc}")

except ValueError:
    print("Apenas digite números!")