preco = float(input("Digite o preço do produto: R$"))
desconto = preco * 0.05
preco_promocional = preco - desconto
print(f"O preço promocional com 5% de desconto é R${preco_promocional:.2f}.")
