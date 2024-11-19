#Forma um triângulo, o tipo ou não forma um triângulo.
a = float(input("Informe o valor do lado1= "))
b = float(input("Informe o valor do lado2=  "))
c = float(input("Informe  valor do lado3= "))
if a<b+c and b<a+c and c>a+b :
    print("os valores informados formam um triangulo")
    if a==b and a==c :
         print("EQUILÁTERO")
    elif a!=b and a!=c and b!=c :
        print("ESCALENO")
    else:
        print("ISÓSCELES")
else:
     print("os valores informados não formam um triangulo1")   
