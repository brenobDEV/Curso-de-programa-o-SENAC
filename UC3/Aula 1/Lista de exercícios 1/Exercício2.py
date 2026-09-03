""" 2. Verificador de Acesso (Login): Crie uma lógica simples de autenticação. Defina duas
variáveis fixas: username_cadastrado = "admin" e senha_cadastrada = "1234".
Em seguida, use o input() para receber um nome de usuário e uma senha do teclado.
● Se ambos forem iguais aos cadastrados, exiba: "Acesso concedido".
● Caso contrário, exiba: "Credenciais inválidas".
 """
#------------------------------------------------------------------------------------------------#


user = "admin"
senha = "hello world"
x=0

user_teste = input(f"Digite seu nome de usuário: ")
if user_teste == user: 
    while x<=3: 
        senha1 = input(f"Digite sua senha: ")
        if senha1 == senha:
            print(f"Acesso concedido!")
            break
        else: 
            x+=1
            print(f"senha incorreta. Você possui ({x}/3) Tentativas")
           
else:   
    print("Usuário não cadastrado")