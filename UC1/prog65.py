class Biscoito:
    def __init__(self, sabor, gosto):
        self.sabor = sabor 
        self.gosto = gosto
    
    def croc(self):
        return f'{self.gosto} Faz CROC CROC'

biscoito1 = Biscoito("Energético", "energia")
print(f"Seu biscoito de saBOR {biscoito1.sabor} que tem gosto de {biscoito1.croc()} ")