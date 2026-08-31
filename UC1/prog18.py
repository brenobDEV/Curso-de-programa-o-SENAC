nome = input("Seja bem vindo ao nosso site de alistamento militar... Poderia nos informar o seu nome? ")
data = int(input(f" {nome} Insira seu ano de nascimento "))
idade = 2026 - data
sexo =  input("Agora insira o seu sexo. Digite (M) para masculino e (F) para feminino.").upper()
if sexo == "M" and idade >=18:
    print("Você está apto para o alistamento militar")
else:
    print(f"Você não é apto para o alistamento militar pois você tem {idade} anos e é do sexo {sexo}")

