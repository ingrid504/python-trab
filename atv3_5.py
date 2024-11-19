# Solicitar as informações do usuário
tipo_carro = input("Digite o tipo de carro alugado (popular ou luxo): ").strip().lower()
dias = int(input("Digite o número de dias de aluguel: "))
km_percorridos = int(input("Digite o número de Km percorridos: "));

# Definir as tarifas de aluguel e custo por km de acordo com o tipo de carro
if tipo_carro == "popular":
    aluguel_diario = 90
    if km_percorridos <= 100:
        custo_km = 0.20
    else:
        custo_km = 0.10
elif tipo_carro == "luxo":
    aluguel_diario = 150
    if km_percorridos <= 200:
        custo_km = 0.30
    else:
        custo_km = 0.25
else:
    print("Tipo de carro inválido!")
    exit()

custo_aluguel = aluguel_diario * dias
custo_km_total = km_percorridos * custo_km
total_a_pagar = custo_aluguel + custo_km_total
print(f"Preço do aluguel: R$ {custo_aluguel:.2f}")
print(f"Preço pelo Km percorrido: R$ {custo_km_total:.2f}")
print(f"Total a pagar: R$ {total_a_pagar:.2f}")
