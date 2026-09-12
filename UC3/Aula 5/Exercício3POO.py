'''Exercício 3: Planos de Assinatura (Foco em Herança)
Contexto: Evite a repetição de código (Princípio DRY) reaproveitando atributos e métodos
comuns através de uma hierarquia de classes.
Tarefas:
1. Crie uma classe mãe chamada AssinaturaBase com o atributo usuario e um
método calcular_preco(self) que simplesmente retorna o valor 0.0.
2. Crie uma classe filha chamada AssinaturaPremium que herda de
AssinaturaBase. Sobrescreva (recrie) o método calcular_preco(self)
dentro dela para que retorne o valor 49.90.
3. Crie outra classe filha chamada AssinaturaEstudante que também herda de
AssinaturaBase. Sobrescreva o método calcular_preco(self) para que
retorne o valor 24.90.
4. Teste instanciando um objeto de cada plano e imprimindo o preço final de cada um.'''

class AssinaturaBase:
    def __init__(self, usuario):
        self.usuario = usuario
    
    def calcular_preco(self, valor):
        valor = 0.0
        return f'{valor}'
    
class AssinaturaPremium(AssinaturaBase):
    def __init__(self):
        super().__init__(usuario)
    
    def calcular_preco(self, valor):
        valor = 49.90
        return f'{valor}'

class AssinaturaEstudante(AssinaturaBase):
    def __init__(self):
        super().__init__(usuario)
    
    def calcular_preco(self, valor):
        valor = 24.90
        return f'{valor}'
    

usuario = AssinaturaBase("brenao")
usuario2 = AssinaturaPremium()
usuario3 = AssinaturaEstudante()

print(usuario.calcular_preco(0))
print(usuario2.calcular_preco(0))
print(usuario3.calcular_preco(0))

