c = {}
for i in range(2):
    carro = input("Digite o modelo do carro - ")
    print("--------------------------------------------------")
    marca = input("Digite a marca do carro - ")
    print("--------------------------------------------------")
    valor = float(input("Digite o valor do carro: "))
    c[carro] =  {
        "marca" : marca,
        "valor": valor
    }
    
    print("--------------------------------------------------")
    print("--------------------------------------------------")
    print(f"Dicionario - {c}")
    