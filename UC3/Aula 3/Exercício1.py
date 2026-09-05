'''Exercício 1: O Catálogo de Streaming
Tema: Entretenimento
Vamos criar o modelo de dados básico de uma plataforma como a Netflix.
Tarefa:
1. Crie uma classe chamada Filme.
2. No método __init__, ela deve receber o titulo e a duracao (em minutos).
3. Todo filme deve nascer com um atributo assistido definido como False.
4. Crie um método chamado marcar_como_assistido(self) que simplesmente
muda o atributo assistido para True e imprime: "O filme [nome_do_filme] foi
assistido!"
Teste: Crie dois filmes. Marque apenas o primeiro como assistido. Imprima o atributo
assistido de ambos para confirmar se apenas um mudo'''

#----------------------------------------------------------------------------------------------------#

class Filme:
    def __init__ (self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao
        self.assistido = False

    def marcar_como_assistido(self):
        self.assistido = True 
        return f"O filme {self.titulo} foi assistido"


filme1= Filme("Senhor dos Anéis", 178)
filme2 = Filme("As Branquelas", 120)
filme1.marcar_como_assistido()
catalogo=[filme1, filme2]
total_assistidos = 0

x = input(f"Você deseja conferir seus filmes assistidos? [s/n]\n->").lower()
if x == "s":
    for i in catalogo:
         if i.assistido:
            print(f"- {i.titulo}")
            total_assistidos += 1
    print(f"\nVocê tem um total de {total_assistidos} filme(s) assistido(s).")


   
