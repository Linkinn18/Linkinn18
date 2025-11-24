# Declarando as Funções
def captura_valor():
    while True:
        try:
            valor = int(input("Digite o valor: "))
            return valor
        except ValueError:
            print("Só é permitido números!")
            break

def somar(): # Cria função de soma
    valor1 = captura_valor()
    valor2 = captura_valor()

    resultado = valor1 + valor2
    return resultado # Retorna o resultado para ser utilizado fora

def subtracao(): 
    valor1 = captura_valor()
    valor2 = captura_valor()

    resultado = valor1 - valor2
    return resultado 

def multiplicacao(): 
    valor1 = captura_valor()
    valor2 = captura_valor()

    resultado = valor1 * valor2
    return resultado 

def divisao(): 
    valor1 = captura_valor()
    valor2 = captura_valor()
    while True:
        try:
            resultado = valor1 / valor2 
        except ZeroDivisionError:
            print("Divisão por zero não permitido")
            break
        return resultado

# Iniciando as contagem
print("Escolha uma Ação a ser Realizada")
print("1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")
operacao = int(input("Escolha a operação a fazer: "))

if operacao == 1:
    print("#---Adição---#")
    resultado = somar()
    print(f"Seu resultado é: {str(resultado)}") #Apenas um print comum
elif operacao == 2:
    print("#---Subtração---#")
    resultado = subtracao()
    print(f"Seu resultado é: {str(resultado)}") #Apenas um print comum
elif operacao == 3:
    print("#---Multiplicação---#")
    resultado = multiplicacao()
    print(f"Seu resultado é: {str(resultado)}") #Apenas um print comum
elif operacao == 4:
    print("#---Divisão---#")
    resultado = divisao()
    print(f"Seu resultado é: {str(resultado)}") #Apenas um print comum