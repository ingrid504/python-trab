ano_atual = int(input("Digite o ano atual: "))
nascimento = int(input("Digite o ano de nascimento: "))
idade = ano_atual - nascimento

if idade >= 16:
    print(f"Pode votar! Sua idade é {idade} anos.")
else:
    print(f"Não pode votar. Sua idade é {idade} anos.")
