try:    
    temperatura = float(input("Digite uma temperatura em Celcius: "))

    if temperatura >= 30:
        print("Está quente!")
    elif temperatura >= 20:
        print("Está agradavél.")
    elif temperatura >= 10:
        print("Está frio.")

    else:
        print("Está muito frio!")

except ValueError:
    print("Digite apenas números!")