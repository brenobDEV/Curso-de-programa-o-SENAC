""" 5. Filtro de Usuários Ativos: Dado o seguinte "banco de dados" fictício:
Python
usuarios = [
{"id": 1, "nome": "Ana", "email": "ana@email.com", "ativo": True},
{"id": 2, "nome": "Beatriz", "email": "bea@email.com", "ativo": False},
{"id": 3, "nome": "Carlos", "email": "car@email.com", "ativo": True}
]
Tarefa: Escreva um laço for que percorra esta lista e crie uma nova lista chamada
emails_ativos contendo apenas os e-mails dos usuários onde "ativo" é True. No
final, imprima a lista de e-mails """
#-------------------------------------------------------------------------------------#


usuarios = [
    {"id": 1, "nome": "Ana", "email": "ana@email.com", "ativo": True},
    {"id": 2, "nome": "Beatriz", "email": "bea@email.com", "ativo": False},
    {"id": 3, "nome": "Carlos", "email": "car@email.com", "ativo": True}
]

for emails_ativos in usuarios:
    if emails_ativos["ativo"] == True:
        print(emails_ativos["email"]) 
   