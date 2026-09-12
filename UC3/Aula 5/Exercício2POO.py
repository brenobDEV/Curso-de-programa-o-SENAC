'''Exercício 2: O Botão Único (Foco em Abstração)
Contexto: Abstração significa esconder a complexidade. Quem usa o seu objeto só quer o
resultado final, sem precisar saber os detalhes difíceis de "como" o trabalho foi feito por
baixo dos panos.
Tarefas:
1. Crie uma classe ProcessadorDePagamento.
2. Crie três métodos internos (apenas com print para simular a ação):
○ _conectar_banco(self) -> Imprime "Conectando ao banco de dados..."
○ _autenticar_token(self) -> Imprime "Autenticando transação..."
○ _deduzir_saldo(self, valor) -> Imprime "Deduzindo R$ [valor] do
saldo...
3. Crie um método público chamado processar_compra(self, valor). Esse é o
único método que o usuário da classe vai chamar de fora.
4. Regra: Dentro do método processar_compra, chame os 3 métodos internos na
ordem correta para efetuar a compra e imprima "Compra finalizada com sucesso".
'''

class ProcessadorDePagamento:

    def _conectar_banco(self):
        print("Conectando ao banco de dados...")

    def _autenticar_token(self):
        print("Autenticando transação...")
    
    def _deduzir_saldo(self, valor):
        print(f"Deduzindo R$ {valor} do saldo...")
    
    def processar_compra(self, valor):
        self._conectar_banco()
        self._autenticar_token()
        self._deduzir_saldo(valor)
        print("Compra finalizada com sucesso")


usuario = ProcessadorDePagamento()
usuario.processar_compra(100)
