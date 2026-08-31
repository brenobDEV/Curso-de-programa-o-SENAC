cargo = input("Insira o seu cargo na empresa: ").lower()


if cargo == "caixa":
      print("Seu salário inicial é de 1500 reais")
      s=1500
elif cargo == "vendedor":
      print("Seu salário inicial é de 2400 reais")
      s=2400
elif cargo == "gerente":
      print("Seu salário inicial é de 4000 reais")
      s= 4000
    
else:
       s= 0
      print("Seu cargo não consta no nosso sistema")


inss = s*0.12
sinss = s - inss

if s >=2000:
      irrf = s * 0.14
      ofc = sinss - irrf
      print(f" seu salario sem inss e irrf é igual a {ofc} os impostos são: irrf igual a {irrf} e inss igual a {inss}")

else:
      irrf = s*0.08
      ofc= sinss - irrf
      print(f"Seu salario sem inss e irrf é igual a {ofc} os impostos são irrf igual a: {irrf} e inss igual a: {inss}")