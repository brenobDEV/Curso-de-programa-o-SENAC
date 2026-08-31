
class alunos:
    def __init__(self, nome, media, status):
        self.nome = nome
        self.media = media
        self.status = status

while True:
    try:
        print("=== Sistema de aprovação do Boletim Escolar ===")
        print("-" *80)
        print("")
        nome = input("Digite o nome e sobrenome do aluno - ")
        nota1 = float(input("Insira a nota do primeiro bimestre - "))
        nota2 = float(input("Insira a nota do segundo bimestre - "))
        nota3 = float(input("Insira a nota do terceiro bimestre - "))
        nota4 = float(input("Insira a nota do quarto bimestre - "))
        mediaf = (nota1+nota2+nota3+nota4)/4
        if mediaf >= 7:
            status = "Passou de ano!"
        elif mediaf <=5:
            status = "Reprovado"
        else:
            status =  "Recuperação"
        
        alunos1 = alunos(nome, mediaf, status)
        
        print("-" *80)
        print(alunos1.nome,"|", alunos1.media,"|", alunos1.status)
        
        
        sair = input("Você deseja parar o programa? caso queira sair digite 'sair' - ").upper()
        if sair == "SAIR":
            break
        else:
            continue
    except ValueError:
        print("Digite somente números na media")