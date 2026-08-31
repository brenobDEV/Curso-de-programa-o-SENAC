def idade_ano(i1):
    return 2026-i1

def se(v1):
    if v1 < 18:
        print("Você é menor de idade :(")
    elif v1 >= 60:
        print("Você é idoso man :P ")
    else:
        print(" você é maior de idade.")
        

ano=int(input("Qual o ano de seu nascimento? - "))
idade = idade_ano(ano)
se(idade)
