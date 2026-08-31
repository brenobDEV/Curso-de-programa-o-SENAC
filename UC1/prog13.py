nome = input("Qual é o seu nome? ")
aidade = int(input(f"Olá {nome} digite aqui o ano de seu nascimento: "))
idade = 2026 - aidade
if idade >= 18:
    print(f"{nome} você é maior de idade por ter {idade} anos.")
else:
    print(f"{nome} você é menor de idade por ter {idade} anos.")