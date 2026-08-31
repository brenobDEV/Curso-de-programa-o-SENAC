while True:
    try:
        numero = int(input("Digite o número para saber a metade"))
        metade = numero/2

        print(f"A metade do número {numero} é {metade}")
        break
    except ValueError:
        print("Erro: Você digitou letras. por favor, digite um número inteiro!")
        