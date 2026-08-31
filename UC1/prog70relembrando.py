ano = int(input("Digite o seu ano de nascimento"))
idade = 2026 - ano

if idade <= 65:
    print(f"Sua idade é {idade}, você é bem idoso")
elif idade  >=18:
    print(f"Sua idade é {idade}, você é maior de idade")
else:
    print(f"Sua idade é {idade}, você é menor de idade")