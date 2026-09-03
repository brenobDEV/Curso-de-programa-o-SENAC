""" 6. Limpeza de Dados de Frete: Um sistema enviou uma lista de fretes, mas alguns valores
estão negativos por erro de processamento:
Python
fretes = [15.50, -2.00, 10.00, 25.00, -5.50, 30.00]
Tarefa: Crie um script que percorra a lista e exiba apenas os valores positivos. """
#---------------------------------------------------------------------------------------------#


fretes = [15.50, -2.00, 10.00, 25.00, -5.50, 30.00]

valores_positivos = []
for i in fretes:
    if i > 0:
        valores_positivos.append(i)
    
print(valores_positivos)