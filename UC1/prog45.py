y = 0
senha = ""
while senha != 0:
    senha = int(input("Digite o número que você quer somar | [0 - Para sair] | - "))
    y = senha + y
    print(f" Número atual: {y} ")
    if senha == 0:
        break
    
