try:
    numerador = int(input("Digite o número para ser dividido "))
    denominador = int(input("Digite o valor da divisão" ))

    resultado = numerador/denominador
    print(f"O resultado é {resultado}")
    
except ValueError:
    print("Digite apenas números inteiros")

except ZeroDivisionError:
    print("Impossível, não consigo fazer uma divisão por 0")