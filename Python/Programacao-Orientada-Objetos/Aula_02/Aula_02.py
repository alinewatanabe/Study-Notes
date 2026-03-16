# Importando Modulos
from os import system
from time import sleep
from math import sqrt
from cmath import sqrt as csqrt

# Definindo Funções
def Menu():
    """Mostra o menu de opcoes"""
    print("-------- Calculadora --------\n")
    print("1 - Soma")
    print("2 - Subtracao")
    print("3 - Multiplicacao")
    print("4 - Divisao")
    print("5 - Raiz Quadrada")
    print("-----------------------------\n")
    
def Soma(n1, n2):
    """Soma duas variaveis"""
    resultado = n1 + n2
    print(f"A soma de {n1} e {n2} é {resultado}")

def Subtracao(n1, n2):
    """Subtrai duas variaveis"""
    resultado = n1 - n2
    print(f"A subtracao de {n1} e {n2} é {resultado}")

def Multiplicacao(n1, n2):
    """Multiplica duas variaveis"""
    resultado = n1 * n2
    print(f"A multiplicacao de {n1} e {n2} é {resultado}")

def Divisao(n1, n2):
    """Divide duas variaveis"""
    resultado = n1 / n2
    print(f"A divisao de {n1} e {n2} é {resultado}")

def RaizQuadrada(n1):
    """Calcula a raiz quadrada de uma variavel"""
    if(type(n1) == float):
        resultado = sqrt(n1)
    elif(type(n1) == complex):
        resultado = csqrt(n1)    
    print(f"A raiz quadrada de {n1} é {resultado}")

def Check_Input(n1, n2):
    """Verifica se o input é do tipo float ou numero complexo e altera o tipo da variavel conforme o necessario"""
    try:
        n1 = float(n1)
        n2 = float(n2)
    except ValueError:
        n1 = complex(n1)
        n2 = complex(n2)
    return n1, n2


# Programa Principal
repeat = True

while repeat:
    Menu()
  
    choice = int(input("Digite o numero da operacao desejada: "))

    if choice == 1:
        n1 = input("Digite o primeiro numero: ")
        n2 = input("Digite o segundo numero: ")
        n1, n2 = Check_Input(n1, n2)
        Soma(n1, n2)
    if choice == 2:
        n1 = input("Digite o primeiro numero: ")
        n2 = input("Digite o segundo numero: ")
        n1, n2 = Check_Input(n1, n2)
        Subtracao(n1, n2)
    if choice == 3:
        n1 = input("Digite o primeiro numero: ")
        n2 = input("Digite o segundo numero: ")
        n1, n2 = Check_Input(n1, n2)
        Multiplicacao(n1, n2)
    if choice == 4:
        n1 = input("Digite o numerador: ")
        n2 = input("Digite o denominador: ")
        n1, n2 = Check_Input(n1, n2)
        Divisao(n1, n2)
    if choice == 5:
        n1 = input("Digite o numero: ")
        n2 = 0
        n1, n2 = Check_Input(n1, n2)
        RaizQuadrada(n1)

    repeat = input("Você deseja fazer outra operacao? (s/n): ").lower()
    if repeat == "n":
        repeat = False
        print("Encerrando...")
        sleep(2)
    system("cls") # Caso o programa utilizado seja o replit, substituir por "clear"
