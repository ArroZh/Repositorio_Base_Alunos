print("-----------------------------")
print("SISTEMA DA BIBLIOTECA")
print("-----------------------------")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
possui_cartão = input("Possui cartão da biblioteca? \n (1-sim / 2-não)")

if idade >= 18:
    if possui_cartão == "1":
         print("Cadastro realizado com sucesso! ")
    else:
        print("Você não pode se cadastrar. ") 
else:
    print("REQUISITAMOS QUE SEJA MAIOR DE IDADE E TENHA CARTãO 👻")