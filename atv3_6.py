 Função para calcular pontos e dinheiro
def calcular_pontos_e_dinheiro(horas_atividade):
    if horas_atividade <= 10:
        pontos = horas_atividade * 2
    elif horas_atividade <= 20:
        pontos = 10 * 2 + (horas_atividade - 10) * 5
    else:
        pontos = 10 * 2 + 10 * 5 + (horas_atividade - 20) * 10

 
   dinheiro = pontos * 0.05
    return pontos, dinheiro

horas_atividade = float(input("Digite as horas de atividade no mês: "))
pontos, dinheiro = calcular_pontos_e_dinheiro(horas_atividade)

print(f"Você ganhou {pontos} pontos.")
print(f"O valor em dinheiro que você conseguiu é R${dinheiro:.2f}")
