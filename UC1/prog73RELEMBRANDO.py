compra = []
n = ""
valor = "0"
while n != 0:
    n = input("Digite o nome do item ou digite 0 pra sair - ")
    x = float(input("Digite o valor do item para adiciona-lo à comanda. "))
    compra.append(n)
    valor += n 
    total = valor *1.10
    print(total)
    print(compra)
    