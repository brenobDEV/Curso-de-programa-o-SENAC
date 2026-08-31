cursos = ["Python", "Excel"]

def atuais():
    for i in cursos:
        print(f"Esses foram seus cursos atuais: {i}")

atuais()
print("-" * 100)
mi = input("Digite um item que você queira adicionar na lista")
print(f"{mi} - Adicionado")
cursos.append(mi)
atuais()
print("-" * 100)
ti = input("Digite um item que você queira retirar da lista")
print(f"{ti} - Removido")
cursos.remove(ti)
atuais()
print("-" * 100)
cursos.sort
print(f"Cursos organizados. - ")
atuais()
