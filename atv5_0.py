pares = 0
impares = 0
contador = 0

while contador < 6:
    numero = int(input("Digite um número: "))
    
    if numero % 2 == 0:
        pares += 1  
    else:
        impares += 1  
    
    contador += 1
    
print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)
