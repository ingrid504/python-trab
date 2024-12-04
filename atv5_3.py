Desafios
import random
numero_sorteado = random.randint(1, 100)
tentativas = 0 

while tentativas < 10:
    chute = int(input("digite seu chute: "))
    tentativas += 1
    if chute > numero_sorteado:
        print ("chute maior que o numero sorteado: ")
    if chute < numero_sorteado:
        print ("chute menor que o numero sorteado: ")
    else : 
        print ("voce acertou")
        break
if tentativas ==10: 
    print ("acabou seus chutes, o numero correto era", numero_sorteado)

desafio 2

def votar():
    votos_candidato_a = 0
    votos_candidato_b = 0
    votos_candidato_c = 0
    votos_candidato_d = 0
    votos_brancos = 0
    votos_nulos = 0
    total_votantes = 0

    while True:
        try:
            voto = int(input("Digite seu voto (1-Candidato A, 2-Candidato B, 3-Candidato C, 4-Candidato D, 5-Voto em Branco): "))
        except ValueError:
            print("Entrada inválida! Digite um número entre 1 e 5.")
            continue

        if voto == 1:
            votos_candidato_a += 1
        elif voto == 2:
            votos_candidato_b += 1
        elif voto == 3:
03/12/2024
#no python criar uma aplicação de defina uma lista com o nome dos alunos da turma. e em seguida faça o sorteio de um dos nomes da lista.
#2 refaça o exercicio anterior para ler a quantidade de nomes para sortear. exemplo: Quantos nomes deseja sortear ? 5. entao, devera ser feito 5 sorteios dentro da lista

#exercicio1
import random
alunos = ['Natan', 'Yasmin', 'Debora', 'Ingrid', 'Luane', 'Batista']

nome_sorteado = random.choice(alunos)

print(f'O nome sorteado foi: {nome_sorteado}')

#exercicio2
import random

alunos = ['Natan', 'Yasmin', 'Debora', 'Ingrid', 'Luane', 'Batista']

quantidade = int(input('Quantos nomes deseja sortear? '))

if quantidade > len(alunos):
    print(f'O número de nomes a serem sorteados é maior do que o número de alunos. Temos apenas {len(alunos)} alunos.')
else:
    print('Nomes sorteados:')
    for  in range(quantidade):
        nome_sorteado = random.choice(alunos)
        print(nome_sorteado)

#exercicio3                     
# Criar um jogo de pedra, papel e tesoura no qual o computador é um dos jogadores (por isso falei da biblioteca random antes de jogar o desafio). Ao final de cada jogada o computador deverá perguntar Qual sua opção de jogada ?1- Pedra 2 Papel 3 Tesoura Você escolheu Pedra e o computador PedEMPATE jogar novamente (S/N) ?
import random

def escolha_computador():
    return random.choice(["Pedra", "Papel", "Tesoura"])

def resultado(jogada_usuario, jogada_computador):
    if jogada_usuario == jogada_computador:
        return "EMPATE"
    elif (jogada_usuario == "Pedra" and jogada_computador == "Tesoura") or \
         (jogada_usuario == "Papel" and jogada_computador == "Pedra") or \
         (jogada_usuario == "Tesoura" and jogada_computador == "Papel"):
        return "VOCÊ VENCEU"
    else:
        return "COMPUTADOR VENCEU"

def jogar():
    while True:
        print("Qual sua opção de jogada ?")
        print("1- Pedra")
        print("2- Papel")
        print("3- Tesoura")

        opcao = input("Opção: ")

        if opcao == '1':
            jogada_usuario = "Pedra"
        elif opcao == '2':
            jogada_usuario = "Papel"
        elif opcao == '3':
            jogada_usuario = "Tesoura"
        else:
            print("Opção inválida. Tente novamente.")
            continue

        jogada_computador = escolha_computador()
        print(f"Você escolheu {jogada_usuario} e o computador escolheu {jogada_computador}")

        resultado_jogo = resultado(jogada_usuario, jogada_computador)
        print(f"Resultado: {resultado_jogo}")

        jogar_novamente = input("Jogar novamente (S/N)? ").strip().upper()
        if jogar_novamente != 'S':
            print("Obrigado por jogar!")
            break
jogar()
