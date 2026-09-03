""" 7. Contagem de Estoque Crítico: Dada a lista de quantidades em stock: itens_estoque
= [12, 3, 8, 2, 15, 4, 20]. Tarefa: Escreva um código que conte quantos produtos
têm menos de 5 unidades e exiba o total """
#----------------------------------------------------------------------------------------------#

itens_estoque = [12, 3, 8, 2, 15, 4, 20]
contador_critico = 0 

for i in itens_estoque:
    if i < 5:
        contador_critico += 1  

print(contador_critico)