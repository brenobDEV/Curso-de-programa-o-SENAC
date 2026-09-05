'''Exercício 4: O Sistema de Transferência
Tema: FinTech (Interação entre Objetos)
Chegou a hora de fazer um objeto interagir diretamente com outro objeto! Vamos simular
uma transferência via PIX entre duas contas diferentes.
Tarefa:
1. Crie uma classe chamada CarteiraDigital.
2. O método __init__ deve receber o nome_titular e o saldo_inicial.
3. Crie um método chamado transferir_pix(self, valor,
carteira_destino). O parâmetro carteira_destino será outro objeto da
mesma classe CarteiraDigital.
4. Regra de negócio dentro do método:
○ Verifique se o objeto atual (self) tem saldo suficiente para a transferência
(self.saldo >= valor).
○ Se tiver dinheiro: Subtraia o valor do saldo atual (self) e some esse
mesmo valor ao saldo da carteira_destino. Imprima uma mensagem de
sucesso ("Transferência de R$ X realizada com sucesso!").
○ Se não tiver dinheiro: Imprima "Erro: Saldo insuficiente para realizar o PIX."
Teste: * Crie a carteira do cliente_a com R$ 500.00 de saldo.
● Crie a carteira do cliente_b com R$ 100.00 de saldo.
● Faça o cliente_a transferir R$ 150.00 para o cliente_b. (Exemplo de uso:
cliente_a.transferir_pix(150.00, cliente_b))
● Imprima o saldo final das duas carteiras para confirmar se o cliente_a ficou com
R$ 350.00 e o cliente_b com R$ 250.00.'''

class CarteiraDigital:
    def __init__(self, nome_titular, chave_pix):
        self.nome_titular = nome_titular
        self.saldo_inicial = 0.0
        self.chave_pix = chave_pix

    def fazer_pix(self,valor,chave_pix):
        if valor <= self.saldo_inicial:
            self.saldo_inicial -= valor
            chave_pix.saldo_inicial += valor
            return f"Trasferência de {valor} reais concluida. Para {chave_pix.nome_titular}, chave pix {self.chave_pix}"
        else:
            return f"Transferência não concluída: Saldo insuficiente."
        
    def consulta(self):
        return f"Seu saldo atual é de {self.saldo_inicial}"

conta1 = CarteiraDigital("Gustavo", 219)
conta2 = CarteiraDigital("Tony", 218)
conta2.saldo_inicial = 100.00
conta1.saldo_inicial = 500.00
print(conta1.fazer_pix(150.00, conta2))
print(conta1.consulta())
print(conta2.consulta())


