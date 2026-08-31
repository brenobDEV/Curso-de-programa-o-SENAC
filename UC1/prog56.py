def montar_carrinho():
    # 1.criamos a lista vazia, o carrinho
    carrinho = []

    print("=== BEM-VINDO AO SUPERMERCADO PYTHON ===")  

    #laço de repetição para capturar multiplos itens 
    while True:
        produto = input("Digite um produto ou digite 'sair' ")

        # Se o usuario quiser sair, interromper o laço
        if produto.lower() == 'sair':
            break
        
    #Adiciona o produto digitado ao final da lista
        carrinho.append(produto)
        print(f"-> '{produto}' adicionado ao carrinho com sucesso\n")
    
    #Exibe o resultado final
        print("\n=== SEU CARRINHO DE COMPRAS ===")
        if len(carrinho) == 0:
            print("Seu carinho está vazio")
        else:
            #Exibe os itens um embaixo do outro
            for item in carrinho:
                print(f"- {item}")
        print(f"\nTotal de itens no carrinho {len(carrinho)}")

#estando a função
montar_carrinho()