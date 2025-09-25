cotacao = 5

def real_dolar(reais):
    return reais/cotacao

def dolar_real(dolares):
    return dolares*cotacao

opcao = input("Selecione a opção que deseja:\n" \
"[1 -> Converter de Real para dólar]\n" \
"[2 -> Converter de Dólar para real]")

try:
    if opcao == "1":
     real = float(input("Digite a quantidade de reais que você quer converter: "))
     print(real_dolar(real))

    elif opcao == "2":
      dolar = float(input("Digite a quantidade de dolares que você quer converter: "))
      print(dolar_real(dolar))


    else:
       print("Por favor selecione uma das opções..")

except ValueError:
   print("Digite números, por favor!")