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
   
