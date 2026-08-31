nome = input("Digite aqui o seu nome: ")
print(f"{nome}, digite aqui a temperatura do seu ambiente e direi se está em uma temperatura agradavel")

t = input()
if t < "18":
    print(f"Está muito frio, {nome}, se agasalhe")
elif t >= "18" and t < "30":
    print("Você está uma temperatura agradável :P ")
else:
    print(f"Tá quente pkrai, bora pegar uma prainha {nome}")