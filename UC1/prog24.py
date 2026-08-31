print("Prazer, sou sua calculadora pessoal")
p = int(input("Digite aqui o primeiro número - "))
s = int(input("Digite aqui seu segundo número - "))
print(" ")


numero = int(input(f"Pronto, seus números foram registrados, agora escolha uma operação... (1-Somar / 2- Subtrair / 3- multiplicar / 4- Dividir / 5- Potenciação )").upper())

match numero:
    case 1 | "SOMAR":
        valor=p+s
        print(f"Seu resultado é {valor}")
    case 2 | "SUBTRAIR":
        valor=p-s
        print(f"Seu resultado é {valor}")
    case 3 | "MULTIPLICAR":
        valor=p*s
        print(f"Seu resultado é {valor}")
    case 4 | "DIVISÃO":
        valor=p/s
        print(f"Seu resultado é {valor}")
    case 5 | "POTENCIAÇÃO":
        valor=p**s
        print(f"Seu resultado é {valor}")
    case _:
        print("Operação não encontrada")
print("teste de commit")
print("Teste de push pelo vscode")