import random

def adivinhar_numero():
    numero_sorteado = random.randint(1, 100)
    
    tentativas = 10
    tentativas_feitas = 0  
    
    print("Tente adivinhar o número sorteado entre 1 e 100. Você tem 10 tentativas!")
    
    while tentativas > 0:
        try:
            palpite = int(input(f"Você tem {tentativas} tentativas restantes. Qual é o seu palpite? "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue
        
        tentativas_feitas += 1 
        
        if palpite == numero_sorteado:
            print(f"Você acertou o número em {tentativas_feitas} tentativas!")
            break
        elif palpite < numero_sorteado:
            print("O número digitado é menor que o número sorteado.")
        else:
            print("O número digitado é maior que o número sorteado.")
        
        tentativas -= 1
    
    if tentativas == 0 and palpite != numero_sorteado:
        print(f"Você não acertou! O número sorteado era {numero_sorteado}.")
        print(f"Você fez {tentativas_feitas} tentativas no total.")

adivinhar_numero()
