""" 3. Modelagem de Produto: No back-end, os dados trafegam como JSON (Dicionários em
Python). Crie uma lista chamada estoque contendo 3 dicionários. Cada dicionário deve
representar um produto com as chaves: id, nome, quantidade e preco.
● Após criar a lista, adicione um novo produto usando o método .append().
● Imprima no terminal apenas o nome do segundo produto da lista. """
#-----------------------------------------------------------------------------------#


Lista=[
    {"id": 1, "nome": "maçã", "quantidade": 2, "preco": 10.00},
    {"id": 2, "nome": "Senhor dos anéis", "quantidade": 15, "preco": 600.00},
    {"id": 3, "nome": "Arquitetura de Software", "quantidade": 2, "preco": 350.00}
]

print(Lista[1]["nome"])
#lista.append({"id": len(lista)+1, "nome": "Arquitetura de Software", "quantidade": 2, "preco": 350.00})

while True:
    x = input("Digite uma fruta para adicioná-la a tabela ou digite [s] para sair: ").lower()
    if x == "s":
        print(Lista)
        print("você saiu")
        break
    else:
        Lista.append(x)
        print(Lista)
