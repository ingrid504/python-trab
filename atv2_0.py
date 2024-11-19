ano = int(input("Digite o ano"))
if ano % 4 == 0 and ano % 100 != 0 :
    print("o ano", ano, "e bissexto")
else:
    print("o ano", ano, "nao é bissexto")
