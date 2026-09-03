""" 10. Modularização (Funções): Para evitar repetição de código (Princípio DRY), crie uma
função chamada gerar_boas_vindas(nome).
● A função deve retornar a frase: "Olá, [nome], bem-vindo ao servidor
Python!".
● Teste a função chamando-a e imprimindo o resultad """
#---------------------------------------------------------------------------------------------#

def gerar_boas_vindas(nome):
    return f"Olá, {nome}, seja bem vindo ao servidor Python!"

print(gerar_boas_vindas(input("Digite o seu nome: ")))