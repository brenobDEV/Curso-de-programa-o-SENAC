
conta = 0 
comanda = 1
b = 15
p= 65.99
c = 12.6
print("---COMANDA RESTAURANTE---")
print("Produtos: #001 -> Batata frita (R$ 15.00) | #002 -> Petiscos (R$ 65.99) | #003 -> Chopp (R$ 12.60)") 
print("-" *100)
while comanda != 0:
    comanda = int(input(f"Insira o código do produto | ou digite 0 para fechar a conta. - "))
    if comanda == 1:
        print("O item Batata frita foi adicionado!")
        conta = conta + b
        print("-" * 200)
    elif comanda == 2:
        print("O item Petiscos foi adicionado!")
        conta = conta + p
        print("-" * 200)
    elif comanda ==3:
        print("O item Chopp foi adicionado!")
        conta = conta + c
        print("-" * 200)
    elif comanda ==0:
        percent = input('Você gostaria de acrescentar os "10%" do garçom? (SIM OU NÃO) - ').upper()
        print("-" * 200)
        if percent == "SIM":
            conta = (conta*1,1)
            print(f"O valor final da conta é de R$ {conta: .2f} reais, constando os 10%")
            break
        else: 
             print(f"O valor final da conta é de R$ {conta: .2f} reais, Sem constar os 10% !")
             break
    else:
        print("Produto não encontrado.")
    print("-" * 200)
    print(f"subtotal = R$ {conta: .2f} reais")
