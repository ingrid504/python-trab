inicio = int(input("Digite o primeiro valor: "))
fim = int(input("Digite o último valor: "))
incremento = int(input("Digite o incremento: "))

if incremento == 0:
    print("O incremento não pode ser zero.")
else:
    if inicio < fim and incremento < 0:
        print("Para contagem crescente, o incremento deve ser positivo.")
    elif inicio > fim and incremento > 0:
        print("Para contagem decrescente, o incremento deve ser negativo.")
    else:
        print("Contagem:", end=" ")
        for i in range(inicio, fim, incremento):
            print(i, end=" ")
        print("Acabou!")
