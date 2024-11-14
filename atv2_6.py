a = float(input("Informe o valor do lado 1"))
b = float(input("Informe o valor do lado 2"))
c = float(input("Informe o valor do lado 3"))

if a>b+c and b<a+c and c<a+b :
    print("os valores informados formam um triangulo")
else:
    print("os valores informados não formam um triangulo")
