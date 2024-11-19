peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em metros: "))
imc = peso / (altura ** 2)
print(f"\nSeu IMC é: {imc:.2f}")
if imc < 18.5:
    print("Classificação: Abaixo do peso")
elif 18.5 <= imc < 25:
     print("Classificação: Peso ideal")
elif 25 <= imc < 30:
     print("Classificação: Sobrepeso")
elif 30 <= imc < 40:
    print("Classificação: Obesidade")
else:
    print("Classificação: Obesidade mórbida")
