print("Seja bem vindo(a) à Tech Park...")
nome = input("Por favor insira seu nome ")
idade= int(input("insira sua idade "))
print(" ")

ingresso = input(f"{nome} você por acaso possuí ingresso? (responda com sim ou não): ").upper()
if idade >=12 and ingresso == "SIM":
    print(f"Acesso liberado! SEJA BEM VINDO(A) {nome} Divirta-se com a tech park")
elif idade <12 and ingresso == "SIM":
    print(f"{nome} você possui o ingresso mas infelizmente não conseguirá ingressar na Tech Park por você ter {idade} anos")
else:
    print("ACESSO NEGADO, você precisa de um ingresso")