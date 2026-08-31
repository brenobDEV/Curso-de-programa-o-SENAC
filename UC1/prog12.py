nome = input("Digite seu nome: ")
n1 = float(input("Digite a nota do seu primeiro bimestre: "))
n2 = float(input("Digite a nota do seu segundo bimestre: "))
n3 = float(input("Digite a nota do seu terceiro bimestre: "))
n4 = float(input("Digite a nota do seu quarto bimestre: "))
media = (n1+n2+n3+n4)/4
print(f"{nome} Sua média escola é de aproximadamente {media : .1f}")
if media >= 6:
    print("Parabéns, Você passou de ano!")
else:
    print("Você ficou reprovado")