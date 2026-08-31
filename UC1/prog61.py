carros = []
x=0
while x<=3:
    c1 = input("Digite um nome de um carro ou digite (s) para sair: ")

    if c1.lower() == "s":
        break
    else:
        x=x+1
        
    carros.append(c1)

    print("Essa é sua lista atual:")
    print("-" * 100)
    for carro in carros:
        print(carro)

print("-" * 100)
print("Aqui está sua lista organizada:")

carros.sort()

for carro in carros:
    print(carro)