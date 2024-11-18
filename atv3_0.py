nome = input("Digite o nome: ")
salario = float(input("Digite o salario: "))  # Converte o salário para float
anos = int(input("Digite quantos anos trabalha na empresa: "))  # Converte o número de anos para int

if anos <= 3:
    aumento = salario * 0.03
    faixa_aumento = "3%"
elif 3 < anos < 10:
    aumento = salario * 0.12
    faixa_aumento = "12%"
else:
    aumento = salario * 0.20
    faixa_aumento = "20%"

novo_salario = salario + aumento   
