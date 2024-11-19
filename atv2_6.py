n1 = float (input("Digite a primeira nota"))
n2 = float(input("Digite a segunda nota"))
media = (n1 + n2) / 2  # Corrigindo o cálculo da média

if media < 5:
    print("Reprovado com média:", media)
elif media >= 7:
    print("Aprovado com média:", media)
else:
    print("Recuperação com média:", media)
