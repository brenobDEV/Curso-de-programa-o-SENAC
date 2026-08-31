for i in range(5):
    valor =int(input("Digite um valor que verei se é par ou impar"))
    x = valor % 2
    if x == 1:
        print(f"{valor} é impar")
    else:
        print(f"{valor} é par")
