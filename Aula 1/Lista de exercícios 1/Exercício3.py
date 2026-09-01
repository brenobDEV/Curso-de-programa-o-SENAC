Lista=["banana", "maca"]

print(Lista)

while True:
    x = input("Digite uma fruta para adicioná-la a tabela ou digite [s] para sair: ").lower()
    if x == "s":
        print(Lista)
        print("você saiu")
        break
    else:
        Lista.append(x)
        print(Lista)
