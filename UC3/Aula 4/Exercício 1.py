'''Exercício 1: A Biblioteca Central (Com Histórico de Ações)
Tema: Sistema de gestão de empréstimos de livros. Novo Desafio: O objeto deve guardar
uma lista interna registrando seu histórico de movimentações.
Requisitos:
● Classe Livro:
○ Atributos: codigo, titulo, disponivel (booleano, inicia como True) e
historico_emprestimos (lista vazia).
○ Método emprestar(nome_usuario): Verifica se está disponível. Se sim,
muda para False e adiciona a string "Emprestado para [nome]" na lista de
histórico.
○ Método devolver(): Verifica se está emprestado. Se sim, muda para True
e adiciona "Devolvido ao acervo" no histórico.
○ Método exibir_historico(): Imprime todas as ações registradas na
lista do histórico.
● O Sistema:
○ Menu principal: [1] Listar Livros, [2] Cadastrar Livro, [3]
Selecionar Livro.
○ Submenu do Livro Selecionado: [1] Emprestar, [2] Devolver, [3]
Ver Histórico, [0] Voltar.'''

#---------------------------------------------------------------------------------------------------------#

class Livro:
    def __init__(self, titulo, codigo):
        self.titulo = titulo
        self.codigo = codigo 
        self.disponivel = True
        self.historico = [] 
    
    def emprestar(self, nome_usuario):
        if self.disponivel:
            self.historico.append((f"{nome_usuario} pegou {self.titulo} emprestado"))
            self.disponivel = False
            return f'Você pegou o Livro!'
        else:
            return f'Lamento lhe informar... mas o livro já está emprestado para o usuário de nome {nome_usuario}'
        
    
    def devolver(self,nome_usuario):
        if not self.disponivel:
            self.disponivel = True
            self.historico.append((f"{nome_usuario} devolveu {self.titulo} "))
            return f'Livro {self.titulo}, foi devolvido!'
        else:
            return 'O livro já consta em nosso sistema'
    
    def exibir_historico(self):
        return f'{self.historico}'
    
biblioteca = [
    Livro("senhor dos anéis", 123 ),
    Livro("arsene lupin", 124),
]
    
while True:
    resposta1 = int(input(f"O que você deseja fazer? [1] Listar Livros, [2] Cadastrar Livro, [3] Selecionar Livro. "))
    if resposta1 == 1:
        for i in biblioteca:
            if i.disponivel:
                print(f"{i.titulo} estão disponíveis, códigos {i.codigo}")
            else:
                print("Não há livros disponíveis")
    elif resposta1 == 2:
        titulo = input("Digite o título do Livro que você deseja adicionar: ")
        codigo = int(input("Digite o código do Livro. "))
        novo_livro = Livro(titulo, codigo)
        biblioteca.append(novo_livro)  
    
    elif resposta1 == 3:
        while True:
            resposta2 = int(input("Selecione alguma dessas opções: [1] Emprestar, [2] Devolver, [3] Ver Histórico, [0] Voltar"))
            if resposta2 == 1:
                user = input("Digite seu nome de usuário: ")
                for i in biblioteca:
                    livro_escolhido = int(input("Digite o código do livro que você quer: "))
                    if livro_escolhido == i.codigo:
                        print(i.emprestar(user))
            
            elif resposta2 == 2:
                user = input("Digite seu nome de usuário: ")
                for i in biblioteca:
                    if not i.disponivel:
                        i.disponivel = True
                        print(i.devolver(user))         

            elif resposta2 ==3:
                for i in biblioteca:
                    print(i.exibir_historico())
            elif resposta2 == 0:
                continue
            else:
                print("Erro:Opção_inválida")
                break