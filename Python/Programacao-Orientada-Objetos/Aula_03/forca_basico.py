# Importando as bibliotecas
from random import choice
import os
from time import sleep

# Definindo as funções
def imprime(ponto, certas, erradas, palavra):
    os.system('cls')
    print("*************** Forca ***************")
    print("\n\nPalavra secreta: " + palavra + "\n\n")
    if(ponto == 0):
        print("=======[_] \n||      |  \n||         \n||         \n||         \n||         \nHHHHHHHHHHHH")
    elif(ponto == 1):
        print("=======[_] \n||      |  \n||      o  \n||         \n||         \n||         \nHHHHHHHHHHHH")
    elif(ponto == 2):
        print("=======[_] \n||      |  \n||      o  \n||      |  \n||         \n||         \nHHHHHHHHHHHH")
    elif(ponto == 3):
        print("=======[_] \n||      |  \n||      o  \n||     /|  \n||         \n||         \nHHHHHHHHHHHH")
    elif(ponto == 4):
        print("=======[_] \n||      |  \n||      o  \n||     /|\ \n||         \n||         \nHHHHHHHHHHHH")
    elif(ponto == 5):
        print("=======[_] \n||      |  \n||      o  \n||     /|\ \n||     /   \n||         \nHHHHHHHHHHHH")
    elif(ponto == 6):
        print("=======[_] \n||      |  \n||      o  \n||     /|\ \n||     / \ \n||         \nHHHHHHHHHHHH")

    print("\nLetras erradas:",erradas)
    print("Letras corretas:",certas)

def iniciaPalavra(tamanho):
    return '_'*tamanho

def sorteia():
    return choice(['cachorro', 'gato', 'galinha', 'cavalo', 'camelo', 'girafa', 'elefante', 'pirata', 'rato', 
        'arara', 'arame', 'familia', 'camisa', 'fazenda', 'cama', 'mesa', 'garfo', 'sapato', 'formiga', 'martelo',
         'lagarto', 'lanche', 'copo', 'corpo', 'humano', 'laranja', 'pera', 'melancia', 'manteiga', 'sofa'])
    
def parabens():
    """Parabenisa o jogador caso tenha acertado a palavra secreta"""
    print("\n\nParabéns, você acertou a palavra secreta! :)\n")
    print(f"A palavra secreta era: {palavra_secreta}")
    
def game_over():
    """Da game over caso o jogador tenha errado 6 vezes"""
    print("\n\nGame over! :(\n")
    print(f"A palavra secreta era: {palavra_secreta}")

# Programa principal
jogar ='s'
while(jogar == 's'):
    pontos = 0
    palavra_secreta = sorteia()
    tam = len(palavra_secreta)
    palavra = iniciaPalavra(tam)
    letras_certas = []
    letras_erradas = []
    palavra_traco = []

    while((palavra != palavra_secreta) and (len(letras_erradas) < 6)):
        print(imprime(pontos, letras_certas, letras_erradas, palavra))
        
        chute_letra = input("Digite uma letra: ").lower()
        
        if(len(chute_letra) != 1):
            print("Digite apenas uma letra")
            sleep(2)
            continue
        
        if(chute_letra in palavra_secreta):
            if(chute_letra in letras_certas):
                print("Essa letra já foi digitada, tente outra :)")
                continue
            
            letras_certas.append(chute_letra)
            for i in range(0, tam):
                if(palavra_secreta[i] == chute_letra):
                    palavra = palavra[:i] + chute_letra + palavra[i+1:]             
                    
        else:
            if(chute_letra in letras_erradas):
                print("Essa letra já foi digitada, tente outra :)")
                continue
            letras_erradas.append(chute_letra)
            pontos += 1
            
    if(palavra == palavra_secreta):
        parabens()
    else:
        game_over()
        
    jogar = input("Deseja jogar novamente (s/n)?").lower()

print("Obrigado por jogar :)")
sleep(3)





