class roupa:
    def __init__(self,tipo,cor):
        self.tipo = tipo
        self.cor = cor

    def vestir(self):
        return f' {self.cor} esta cor caiu bem'

roupa1 = roupa("camisa", "branca")
roupa2 = roupa("moletom", "vermelho")

print(f"Sua {roupa1.tipo} é bonita com a cor {roupa1.cor} ")
print(roupa1.vestir())