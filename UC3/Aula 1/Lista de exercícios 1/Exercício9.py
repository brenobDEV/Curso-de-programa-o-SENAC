""" 9. Busca de Usuário por ID:
Python
base_usuarios = [
{"id": 101, "nome": "Alice"},
{"id": 102, "nome": "Bruno"},
{"id": 103, "nome": "Carla"}
]
Tarefa: Peça ao utilizador para digitar um ID. Percorra a lista e, se encontrar o ID, imprima o
nome do usuário. Se o laço terminar e não encontrar, imprima "Usuário não encontrado". """
#------------------------------------------------------------------------------------------------#


base_usuarios = [
{"id": 101, "nome": "Alice"},
{"id": 102, "nome": "Bruno"},
{"id": 103, "nome": "Carla"}
]

def encontrar_id(x):
    encontrado = False
    for i in base_usuarios:
        if x == i["id"]:
            encontrado = True
            print(f"Usuário encontrado: {i['nome']}")

    if not encontrado:
        print("Usuário não encontrado")


encontrar_id(int(input("Digite o Id do usuário que deseja encontrar: ")))

