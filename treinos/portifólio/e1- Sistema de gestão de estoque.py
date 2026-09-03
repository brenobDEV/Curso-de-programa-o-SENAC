print("=== SEU SISTEMA PESSOAL DE GESTÃO ===")
print("    --- Seja bem vindo(a) ---        ")
print("_" * 30)
print()
# cabeçalho.

# Criação da lista e dos itens principais.
lista = []        # Nomes dos produtos
quantidades = []   
precos = []       

# def da lista
def leitura_lista():
    for i in range(len(lista)):
        print(f"[{i}] Produto: {lista[i]} | Qtd: {quantidades[i]} | Preço: R$ {precos[i]:.2f}")

x = ""

print("O que você deseja fazer? ")

while x.lower() != "sair":
    x = input("Para [Cadastrar itens digite - 1] para [registrar entrada ou saída de produtos digite - 2] para [Relatório Geral de Estoques - 3] ou Digite SAIR para sair: ")
    
    if x == "1":
        y = "" 
        while y.lower() != "sair":
            print("\n--- REGISTRO/CADASTRO ---")
            a = input("O que você deseja cadastrar? ")
            b = int(input("Qual a quantidade do item no estoque? ")) 
            c = float(input("Qual o preço unitário do produto? "))
        
            print("-" * 50)
            lista.append(a)
            quantidades.append(b)
            precos.append(c)
        
            print(f"Você já cadastrou {len(lista)} produto(s)")
            print("Seu estoque até agora:")
            leitura_lista()
            print("-" * 50)
            y = input("Se você quiser voltar ao menu digite 'SAIR', caso queira continuar cadastrando produtos digite qualquer coisa: ").lower()
            
    elif x == "2":
        y = "" 
        while y.lower() != "sair":
            print("\n--- REGISTRO DE ENTRADA E SAÍDA ---")
            oqfazer = int(input("O que você deseja fazer? informar a entrada de produtos [1] ou informar a saída de produtos [2]: "))
            
            if oqfazer == 1:
                leitura_lista()
                y = input("Digite o nome do produto ou 'SAIR' para voltar: ")
                if y in lista: #
                    qtd_adicionar = int(input("Quantos itens você deseja adicionar? - "))
                    posicao = lista.index(y) 
                    quantidades[posicao] = quantidades[posicao] + qtd_adicionar
                    print(f"Sucesso! Agora restam {quantidades[posicao]} unidades de {lista[posicao]}.")
                elif y.lower() == "sair":
                    break

            elif oqfazer == 2:
                leitura_lista()
                y = input("Digite o nome do produto ou 'SAIR' para voltar: ")
                if y in lista: 
                    qtd_retirar = int(input("Quantos itens você deseja retirar? - "))
                    posicao = lista.index(y) 
                    if qtd_retirar <= quantidades[posicao]:
                        quantidades[posicao] = quantidades[posicao] - qtd_retirar
                        print(f"Sucesso! Agora restam {quantidades[posicao]} unidades de {lista[posicao]}.")
                    else:
                        print("Quantidade insuficiente no estoque!")
                elif y.lower() == "sair":
                    break
            else:
                print("Ação não encontrada.")

    elif x == "3":
        print("\n--- RELATORIO GERAL ---")
        for i in range(len(lista)):
            if quantidades[i] < 5:
                print(f"Alerta! O produto '{lista[i]}' está com estoque baixo: apenas {quantidades[i]} unidades.")
        print("\nLista completa do estoque:")
        leitura_lista()
        print("Obrigado por usar o nosso sistema de estoque")