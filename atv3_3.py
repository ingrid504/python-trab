# Solicitar as informações necessárias
valor_casa = float(input("Digite o valor da casa: R$ "))
salario = float(input("Digite o salário do comprador: R$ "))
anos = int(input("Digite em quantos anos o empréstimo será pago: "))

# Calcular o valor da prestação mensal
meses = anos * 12
prestacao_mensal = valor_casa / meses

# Verificar se a prestação mensal excede 30% do salário
limite_prestacao = salario * 0.30

# Exibir resultado
if prestacao_mensal <= limite_prestacao:
    print(f"Empréstimo aprovado! A prestação mensal será de R$ {prestacao_mensal:.2f}")
else:
    print(f"Empréstimo negado! A prestação mensal de R$ {prestacao_mensal:.2f} excede 30% do seu salário.")
