nome = input("Digite seu nome: ")
nota_1 = float ( input("Digite a nota 1: "))
nota_2 = float ( input("Digite a nota 2: "))
nota_3 = float ( input("Digite a nota 3: "))

média = (nota_1 + nota_2 + nota_3) / 3

if média >= 7:
    situacao = "Aprovado!"
elif média > 4:
    situacao = "Recuperação."
else:
    situacao = "Reprovado!"                         

print(situacao)



with open ("escola.txt", "a") as arquivo:
    arquivo.write(f"{nome} | {média} | {situacao}\n")