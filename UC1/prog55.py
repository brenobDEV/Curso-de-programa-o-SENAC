def nota_aluno(v1,v2,v3,v4):
    media = (v1+v2+v3+v4)/4
    if media >=7:
        print(f"Aprovado! sua média foi {media: .2f}")
    elif media >= 5:
        print(f"Recuperação! sua média foi {media: .2f}.")
    else:
        print(f"Reprovado! sua média foi {media: .2f}.")

nota1= float(input("Digite sua nota do primeiro bimestre - "))
nota2= float(input("Digite sua nota do segundo bimestre - "))
nota3= float(input("Digite sua nota do terceiro bimestre - "))
nota4= float(input("Digite sua nota do quarto bimestre - "))

nota_aluno(nota1, nota2, nota3, nota4)