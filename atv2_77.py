# Função para calcular a média e mostrar a situação do aluno
def calcular_media():
    # Leitura das duas notas
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = (nota1 + nota2) / 2

    print(f"\nA média do aluno é: {media:.1f}")
    if media <= 4.9:
        print("Situação: REPROVADO")
    elif media >= 5.0 and media <= 6.9:
        print("Situação: RECUPERAÇÃO")
    else:
        print("Situação: APROVADO")
if __name__ == "__main__":
    calcular_media()
