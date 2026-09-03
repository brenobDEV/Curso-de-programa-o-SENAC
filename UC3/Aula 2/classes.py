class Cachorro:
    def __init__(self, nome, raca, tamanho, cor_pelo):
        self.nome = nome
        self.raca = raca
        self.tamanho = tamanho 
        self.cor_pelo = cor_pelo 
        self.patas = 4



zeca = Cachorro("Zeca", "ViraLata", "Médio", "Caramelo")
brutus = Cachorro("Brutus", "Pitbull", "Grande", "Preto")
mel = Cachorro("Mel", "Yorkshire", "Pequeno", "Marrom")

zeca.patas = 3 
print(zeca.nome)

#---------------------------------------------------------------------#

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.ativo = True 
    
    def desativar_conta(self):
        self.ativo = False

    def mudar_nome(self):
        self.nome = input("Digite seu novo nome")

nova_conta = Usuario("Gustavo", "gustavo@email.com")
nova_conta.desativar_conta
print(nova_conta.ativo)