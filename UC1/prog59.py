lista_compras = []
print("-" * 100)
print("=== SuperMercado Guanabis-Python ===")
print("-" * 100)
item=input("Digite um item para adicioná-lo na sua lista de compras -")
print("")

lista_compras.append(item)
for i in lista_compras:
    print(f"Sua lista de compras {i}")