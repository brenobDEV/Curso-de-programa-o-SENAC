dia=input("digite o dia da semana ")
match dia:
    case "segunda" | "terça" | "quarta"| "quinta" | "sexta":
        print("Dia de semana. DIA DE PROGRAMAÇÃO")
    case "sábado" | "domingo":
        print("fim de semana! hora de descansar.")
    case _:
        print("Dia invalido ")