pessoas = {}
for i in range(2):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    pessoas[nome] = idade
    print(f"Cadastro: {pessoas}")