lista_mercado = []
print("=== HIPERMARKET PYTHON! ===")
print("")
while True:
    i1=input(f'Digite o item que quiser adicionar para adicioná-lo a sua lista de compras | Digite "SAIR" para sair ')
    print("")
    if i1 in lista_mercado:
        print("item já cadastrado")

    else:   
        lista_mercado.append(i1)
    if i1.upper() == "SAIR":
        print("você saiu.")
        break
    else:
        lista_mercado.sort()
        print("-" * 100)
        print("Aqui está sua lista de mercado organizada.")
        print("-" * 100)
        for i in lista_mercado:
            print(i)
    