nome = ""
while nome != "SAIR":
    nome = input("Digite seu nome - ").upper()
    if nome =="SAIR":
        break
    print(f" olá {nome} tudo bem?")