import random

def jogar():
    # O computador sorteia um número entre 1 e 5
    numero_sorteado = random.randint(1, 5)

    # Solicita ao jogador que adivinhe o número
    print("Tente adivinhar o número sorteado entre 1 e 5!")
    
    while True:
        try:
            # Leitura da tentativa do jogador
            palpite = int(input("Digite o seu palpite (1 a 5): "))

            # Verificação se o palpite está dentro do intervalo permitido
            if palpite < 1 or palpite > 5:
                print("Por favor, digite um número entre 1 e 5.")
                continue

            # Verifica se o palpite está correto
            if palpite == numero_sorteado:
                print("Parabéns! Você acertou!")
                break
            else:
                print("Errou! Tente novamente.")
        except ValueError:
            print("Por favor, digite um número válido.")

# Função principal para controlar o jogo
def main():
    print("Bem-vindo ao jogo de Adivinhação!")
    
    while True:
        jogar()
        # Pergunta se o jogador quer jogar novamente
        continuar = input("\nDeseja jogar novamente? (s/n): ").lower()
        if continuar != 's':
            print("Obrigado por jogar! Até logo!")
            break

# Inicia o jogo
if __name__ == "__main__":
    main()
