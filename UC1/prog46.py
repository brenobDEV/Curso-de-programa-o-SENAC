
valor = 0 
codiguin = 1
a = 4
f = 7
m = 8
print(f"---SuperMercados Guanabis---")
print("Produtos: #001 -> Arroz (R$ 4.00) | #002 -> Feijão (R$ 7.00) | #003 -> Macarrão (R$ 6.00)")
print("-" * 100)
while codiguin != 0:
    codiguin = int(input("Digite o código para adicioná-lo a sua cesta de compras: - "))
    if codiguin == 1:
        print('O item "Arroz" de  [R$ 4.00] foi adicionado à sua sacola')
        valor =  valor + a
        print("-" * 200)
    elif codiguin == 2:
        print('O item "feijão" de  [R$ 7.00] foi adicionado à sua sacola')
        valor =  valor + f
        print("-" * 200)
    elif codiguin == 3:
        print('O item "Macarrão" de  [R$ 6.00] foi adicionado à sua sacola')
        valor =  valor + m
        print("-" * 200)
    elif codiguin == 0:
        print(f"Valor total da sua sacola está R$ {valor: .2f} de reais")
        break
    else:
      print("Produto não encontrado")
      print("-" * 200)
    