print("Seu programa deu erro? Fique calmo, digite aqui para saber mais")
erro = input(" ")
match erro:
    case "200":
        print("Sucesso! Tudo certo com sua requisição")
    case "400":
        print("Erro do Cliente: Requisição malformada")
    case "401" | "403":
        print(" Erro de permissão: você não tem acesso a esta página.")
    case "404":
        print("Erro: Página não encontrada")
    case "500" | "503":
        print("Erro no servidor: nosso sistema está muito instável no momento.")
    case _:
        print("HTP Status desconhecido")
