
inicio = int(input("Digite o primeiro Valor: "))
fim = int(input("Digite o último Valor: "))
incremento = int(input("Digite o incremento: "))
if incremento == 0:
    print("O incremento não pode ser zero.")
else:
    if incremento > 0 and inicio <= fim:
        print("Contagem:", end=" ")
