def calcular_salario(horas_trabalhadas, valor_hora):
    return horas_trabalhadas * valor_hora

valor_hora = float(input("Digite a quantidade que você ganha por hora: "))
qtd_horas = float(input("Digite a quantidade de horas trabalhadas no mês: "))


salario = calcular_salario(qtd_horas, valor_hora)


print(f"Seu salário do mês é: {salario:.2f}")