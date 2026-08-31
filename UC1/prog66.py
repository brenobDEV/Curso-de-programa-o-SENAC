class Passarinho:
    def __init__(self, raca, cor):
        self.raca = raca
        self.cor = cor

    def canta(self):
        return f'{self.raça} canta'
    
    def dança(self):
        return f'{self.raça} dança'

passarinho1 = Passarinho("Quero-Quero", "verde")
passarinho2 = Passarinho("Bem-te-vi", "Vermelho")

print(f"O passarinho é da raça {passarinho1.raca} e ele é de cor {passarinho1.cor} a raça {passarinho1.canta()}")
print("-" * 80)
print(f"O passarinho é da raça {passarinho2.raca} e ele é de cor {passarinho2.cor} a raça {passarinho2.dança()}")