import random

def jogar():
    # Opções disponíveis para o jogo
    opcoes = ['Pedra', 'Papel', 'Tesoura']

    # Entrada do jogador com validação
    print("Escolha uma opção:")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    
    while True:
        try:
            jogador = int(input("Digite o número correspondente à sua escolha (1, 2 ou 3): "))
            if jogador not in [1, 2, 3]:
                raise ValueError("Escolha inválida. Por favor, escolha 1, 2 ou 3.")
            jogador -= 1  # Ajusta a escolha do jogador para índices de lista
            break
        except ValueError as e:
            print(e)

    # Escolha do computador
    computador = random.randint(0, 2)
    print(f"\nVocê escolheu: {opcoes[jogador]}")
    print(f"O computador escolheu: {opcoes[computador]}")

    # Verificação do vencedor
    if jogador == computador:
        print("Empate!")
    elif (jogador == 0 and computador == 2) or (jogador == 1 and computador == 0) or (jogador == 2 and computador == 1):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

# Loop para jogar várias vezes
def main():
    print("Bem-vindo ao jogo JoKenPo!")
    while True:
        jogar()
        continuar = input("\nDeseja jogar novamente? (s/n): ").lower()
        if continuar != 's':
            print("Obrigado por jogar! Até logo!")
            break

# Inicia o jogo
if __name__ == "__main__":
    main()
