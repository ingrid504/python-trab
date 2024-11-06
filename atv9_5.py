km_percorridos = float(input("Digite a quantidade de Km percorridos: "))
dias_alugados = int(input("Digite a quantidade de dias pelos quais o carro foi alugado: "))
preco_km = km_percorridos * 0.20
preco_dias = dias_alugados * 90
preco_total = preco_km + preco_dias
print(f"O preço total a pagar é R${preco_total:.2f}.")
