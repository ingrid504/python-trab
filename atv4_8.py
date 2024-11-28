def calcular_novo_salario(salario, genero, anos_trabalho):
    if genero == "feminino":
        if anos_trabalho < 15:
            reajuste = 0.05 
        elif 15 <= anos_trabalho <= 20:
            reajuste = 0.12  
        else:
            reajuste = 0.23  
    elif genero == "masculino":
        if anos_trabalho < 20:
            reajuste = 0.03  
        elif 20 <= anos_trabalho <= 30:
            reajuste = 0.13  
        else:
            reajuste = 0.25  
    else:
        raise ValueError("Gênero inválido! Use 'feminino' ou 'masculino'.")
    novo_salario = salario * (1 + reajuste)
    return novo_salario
salario_atual = float(input("Digite o salário atual do funcionário: R$"))
genero = input("Digite o gênero do funcionário (feminino/masculino): ").strip().lower()
anos_trabalho = int(input("Digite o número de anos de trabalho na empresa: "))
novo_salario = calcular_novo_salario(salario_atual, genero, anos_trabalho)
print(f"Novo salário do funcionário: R${novo_salario:.2f}")
