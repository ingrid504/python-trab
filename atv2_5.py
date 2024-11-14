distancia = float(input("informe a distancia em km "))
if distancia <= 200 :
    valor_corrida = distancia * 0.50
else:
    valor_corrida = distancia * 0.45
    print(f"O valor da corrida e R$ {valor_corrida:.2f}")
