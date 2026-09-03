""" 4. Atualização de Status: Imagine que recebeu um objeto de um serviço de entrega:
Python
pedido = {
"cliente": "João Silva",
"prato": "Hambúrguer Artesanal",
"status": "em preparo"
}
Tarefa: Altere o valor da chave "status" para "saiu para entrega" e imprima o
dicionário completo para confirmar a alteração. """
#------------------------------------------------------------------------------------#


pedido = { "id": 1, "cliente": "João Silva",
"prato": "Hambúrguer Artesanal",
"status": "em preparo"
}


pedido["status"] = "Saiu para Entrega"

print(pedido["status"])