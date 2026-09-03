""" 8. Calculadora de Património: Utilizando a lista de produtos que criou no Exercício 3,
percorra o stock e calcule o Valor Total do Património (soma de quantidade * preco
de todos os itens). Exiba o resultado com uma mensagem explicativa. """
#--------------------------------------------------------------------------------------------------#

Lista=[
    {"id": 1, "nome": "maçã", "quantidade": 2, "preco": 10.00},
    {"id": 2, "nome": "Senhor dos anéis", "quantidade": 15, "preco": 600.00},
    {"id": 3, "nome": "Arquitetura de Software", "quantidade": 2, "preco": 350.00}
]

patrimonio = 0 

for i in Lista:
    patrimonio += i["quantidade"] * i["preco"]
print(patrimonio)
