inicio = int(input("Digite o primeiro valor: "))
fim = int(input("Digite o último valor: "))
incremento = int(input("Digite o incremento: "))

if incremento <= 0:
    print("O incremento deve ser maior que zero.")
else:
    print("Contagem:", end=" ")
    for i in range(inicio, fim, incremento):
        print(i, end=" ")

    print("Acabou!")
