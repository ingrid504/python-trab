# Leitura do ano atual e ano de nascimento
ano = int(input("Informe o ano atual: "))
nascimento = int(input("Informe o ano de nascimento: "))
idade = ano - nascimento
if idade < 18:
    print("Faltam", 18 - idade, "anos para você fazer o alistamento.")
if idade == 18:
    print("Você deve se alistar este ano.")
else:
    print("Você já tem", idade - 18, "anos que fez o alistamento.")
