# Leitura de dados
nome = input("Digite seu nome: ")
sexo = input("Digite o sexo (M/F): ")
compra = float(input("Digite o valor da compra: R$ "))  
if sexo.upper() == 'F':
    desconto = compra * 0.13  
    val_desconto = "13%"
else:
    desconto = compra * 0.05  
    val_desconto = "5%"
total_a_pagar = compra - desconto
print(f"Você teve um desconto de {val_desconto}.")
print(f"O valor final a pagar é R$ {total_a_pagar:.2f}.")
