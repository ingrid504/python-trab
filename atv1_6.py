velocidade= float(input("informe a velocidade "))
if velocidade > 80 :
    multa = (velocidade - 80) * 5
    print(f"Velocidade acima de 80 km - multa R$ {multa:.2f} ")
