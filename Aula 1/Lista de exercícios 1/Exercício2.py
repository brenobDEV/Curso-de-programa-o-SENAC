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