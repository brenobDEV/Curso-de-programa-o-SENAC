nome = input("Digite aqui o seu nome: ")
print(f"Olá {nome}, para começarmos a votação, preciso que você escolha um dos candidatos a seguir:")
print("lembre-se do número de seu candidato... 10- Breno; 15- Tony; 20- Gustavo")

votagem = int(input("Em quem você deseja votar para um  Brasil melhor? Digite o número do candidado. "))
if votagem == 10:
    print("Você votou em Breno!")
elif votagem == 15:
        print("Você votou em Tony!")
elif votagem == 20:
        print("Você votou em Gustavo!")
else:
        print("Número invalido")