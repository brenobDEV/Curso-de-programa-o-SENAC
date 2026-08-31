valor = float(input("Digite aqui o valor inicial"))
desconto = float(input("Coloque aqui o número da % de desconto"))
dfinal = desconto / 100
preço = valor * dfinal
print(f"Seu valor final, que iclue o desconto é de aproximadamente: {preço}")
