for i in range(4):
    nome = input("Digite o nome do aluno: ")
    n1 = float(input("Digite a nota do primeiro bimestre do aluno: "))
    n2 = float(input("Digite a nota do segundo bimestre do aluno: "))
    n3 = float(input("Digite a nota do terceiro bimestre do aluno: "))
    m = (n1+n2+n3)/3
    print(f'A média do aluno {nome} é de {m: .1f}, /// notas: "{n1}" | "{n2}" | "{n3}" ')
    print(" ")
    print("-------------------------------------------------------")
    print("-------------------------------------------------------")
    if m >= 7:
        print("Aprovado!")
    elif m >= 5 and m < 7:
        print("Recuperação.")
    else:
        print("Reprovado.")
    print("-------------------------------------------------------")
    print("-------------------------------------------------------")
    print(" ")
a