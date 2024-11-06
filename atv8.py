distancia_m = float(input("Digite uma distância em metros: "))
km = distancia_m / 1000
hm = distancia_m / 100
dam = distancia_m / 10
dm = distancia_m * 10
cm = distancia_m * 100
mm = distancia_m * 1000
print(f"A distância de {distancia_m}m corresponde a:")
print(f"{km} Km")
print(f"{hm} Hm")
print(f"{dam} Dam")
print(f"{dm} dm")
print(f"{cm} cm")
print(f"{mm} mm")
