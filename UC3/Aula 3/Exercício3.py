'''Exercício 3: O App do Banco
Tema: FinTech (Regras de Negócio e Validação)
No backend de um banco, um objeto não pode fazer o que quiser. Precisamos de regras de
negócio (condicionais if/else) dentro dos métodos.
Tarefa:
1. Crie uma classe ContaBancaria que receba no __init__ o nome do titular.
2. O saldo deve começar sempre em 0.0.
3. Crie um método depositar(self, valor). Ele deve somar o valor ao saldo e
imprimir o novo saldo.
4. Crie um método sacar(self, valor). Regra de ouro: O objeto só pode sacar
se o valor for menor ou igual ao saldo.
○ Se houver dinheiro, subtraia do saldo e imprima o valor sacado.
○ Se não houver, imprima "Saque negado: Saldo insuficiente."
Teste: Crie uma conta para você. Deposite R$ 100,00. Tente sacar R$ 150,00 (deve ser
negado). Tente sacar R$ 50,00 (deve ser aprovado).
'''

class ContaBancaria:
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 0.0
    
    def depositar_valor(self, valor):
        self.saldo += valor
        return f" VALOR DEPOSITADO! Seu Saldo atual é de {self.saldo} reais"
    
    def sacar_valor(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            return f"Seu saldo atual é de {self.saldo}" 
        else:
            return "Saque Negado: Saldo insuficiente."
            
conta1 = ContaBancaria("Breno")
print(conta1.depositar_valor(100))
print(conta1.sacar_valor(150))
print(conta1.sacar_valor(50))