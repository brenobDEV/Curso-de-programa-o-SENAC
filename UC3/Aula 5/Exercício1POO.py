'''Exercício 1: O Cofre (Foco em Encapsulamento)
Contexto: No desenvolvimento back-end, não podemos deixar que qualquer parte do
código externo altere dados sensíveis (como uma senha) de forma direta e sem validação.
Tarefas:
1. Crie uma classe Usuario com os atributos login e senha.
2. A senha deve ser definida no momento da criação do objeto (dentro do método
construtor __init__).
3. Crie um método chamado alterar_senha(self, senha_antiga,
nova_senha).
4. Regra: A senha do usuário só deve ser atualizada se o parâmetro senha_antiga
for exatamente igual à senha atual guardada no objeto. Se for igual, atualize a senha
e imprima "Senha alterada com sucesso". Se for diferente, não mude nada e
imprima "Acesso negado: Senha atual incorreta".'''

class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.__senha = senha

    def alterar_senha(self, senha_antiga, nova_senha):
        if senha_antiga == self.__senha:
            self.__senha = nova_senha
            print(nova_senha)
        else:
            print("Senha atual incorreta")


usuarios = Usuario("breno", "123")
usuarios.alterar_senha(input("123"), input("888"))

