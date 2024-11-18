largura = float(input("Informe a largura do terreno: "))
comprimento = float(input("Informe o comprimento do terreno: "))
area = largura * comprimento

if area > 100:
    print("Área do terreno é", area, "m. Terreno popular.")
elif area >= 100 and comprimento < 500:
    print("Área do terreno é", area, "m. Terreno master.")
else:
    print("Área do terreno é", area, "m. Terreno VIP.")
