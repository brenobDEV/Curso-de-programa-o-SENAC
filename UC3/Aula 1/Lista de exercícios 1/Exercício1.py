""" PARTE 1: Condicionais e Regras de Negócio
1. Validador de Checkout: Crie um programa que simule a finalização de uma compra num
e-commerce. O sistema deve receber:
● valor_total (float)
● saldo_usuario (float)
● cupom_valido (booleano - True/False)
Regras:
● Se o cupom for válido, aplique 10% de desconto no valor_total.
● Se o saldo_usuario for maior ou igual ao valor final, exiba: "201 Created -
Pedido realizado com sucesso".
● Caso contrário, exiba: "402 Payment Required - Saldo insuficiente". """
#--------------------------------------------------------------------------------#

valor_total = 100.0
saldo_usuario = 0.0
cupom_valido = True

if cupom_valido:
    valor_total *=  0.9
    print(valor_total)


if saldo_usuario >= valor_total:
    print(f"201 Created - Pedido realizado com sucesso")
else:
    print("402 Payment Required - Saldo insuficiente")
   
