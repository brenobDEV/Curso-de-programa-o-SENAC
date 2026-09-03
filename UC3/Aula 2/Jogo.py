class Personagem:
    def __init__(self, nome, forca):
        self.nome = nome
        self.forca = forca
        self.vida = 100
    
    def atacar(self,alvo):
        alvo.vida -= self.forca


Lula = Personagem("Lula", 9)
Bolsonaro = Personagem("Bolsonaro", 10)

while True:
    Bolsonaro.atacar(Lula)
    Lula.atacar(Bolsonaro)

    if Lula.vida <= 0:
        print(f"{Bolsonaro.nome} venceu!")
        break

    if Bolsonaro.vida <=0:
        print(f"{Lula.nome} Venceu!")
        break