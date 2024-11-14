dias_trabalhados = int(input("Digite o número de dias trabalhados no mês: "))
horas_por_dia = 8
salario_por_hora = 25
salario_total = dias_trabalhados * horas_por_dia * salario_por_hora
print(f"O salário total do mês é R${salario_total:.2f}.")
