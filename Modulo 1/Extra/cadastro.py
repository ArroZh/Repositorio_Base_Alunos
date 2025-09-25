def listar_pessoas(lista):
    print(lista)

def cadastrar_pessoa(lista,nome):
    lista.append(nome)

def excluir_pessoas(lista,nome):
    lista.remove(nome)


agenda = []

## as funções criadas acima são para facilitar o processo abaixo.

print("--------------------------------------------")
print("Bem-vindo ao EasyAgenda.")

nomes = ["samuel"]

while True:
    opcao = input("Digite a opção que deseja: \n"  \
    "[1] - Cadastrar pessoa  \n" \
    "[2] - Listar pessoas  \n"  \
    "[3] - Excluir pessoa   \n" \
    "[0] - Sair \n"
    "  opção:   ")



    if opcao == "1":
        nome = input("Digite o nome de quem voce quer cadastrar: ")
        cadastrar_pessoa(nomes,nome)
        listar_pessoas(nomes)   


    elif opcao == "2":
        print(nomes)


   

    elif opcao == "3":
        nome = input("Digite o nome de quem você deseja deletar: ")
        if nome in nomes:
            nomes.remove(nome)
            listar_pessoas(nomes)
        else:
            print("Nome não encontrado na lista.")

    


    elif opcao == "0":
        break

    else:
        print("Opção inválida!   \n" \
        "Tente novamente.")

print("Obrigada pela preferência.")
print("--------------------------------------------")

    #repetir a opcao q deseja até ser o "sair"