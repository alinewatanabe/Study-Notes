# Definindo as Bibliotecas
from string import ascii_uppercase, digits, punctuation, whitespace
from os import system

# Definindo as Funções
def novos_caracteres():
    """Pede para o usuário criar os caracteres de encriptação"""
    d = {}
    caracteres_inseridos = []
    for i in range(47):
        d[outros[i]] = outros[i]
        caracteres_inseridos.append(outros[i])
        
    for i in range(26):
        novo_caracter = input(f"Digite o caracter correspondente para a letra '{letras[i].lower()}': ")
        while (novo_caracter in caracteres_inseridos):
            print("Caracter já inserido, digite outro\n")
            novo_caracter = input(f"Digite o caracter correspondente para a letra '{letras[i].lower()}': ")
        d[letras[i]] = novo_caracter
        caracteres_inseridos.append(novo_caracter)     
    
    return d

def encriptacao(mensagem, conversor):
    """Encripta uma mensagem com base em um conversor de caracteres"""
    mensagem_encriptada = ""
    for i in range(len(mensagem)):
        mensagem_encriptada += conversor[mensagem[i]]
        
    return mensagem_encriptada

def decriptacao(mensagem, conversor):
    """Decripta uma mensagem com base em um conversor de caracteres"""
    mensagem_decriptada = ""
    chaves = list(conversor.keys())
    valores = list(conversor.values())
    for i in range(len(mensagem)):
        mensagem_decriptada += chaves[valores.index(mensagem[i])]
        
    return mensagem_decriptada

def imprimir(frase_original, mensagem_encripitada, mensagem_decriptada):
    """Imprime a mensagem original, a encriptada e a decriptada"""
    print(50*"-")
    print(f"A frase original foi: {frase_original}\n\n")
    print(f"A frase encriptada é: {mensagem_encripitada}\n\n")
    print(f"A frase decriptada é: {mensagem_decriptada}\n")
    print(50*"-")
    
def verificacao(mensagem_original, mensagem_decripitada):
    """Verifica se a mensagem original é a mesma que a decriptada"""
    for i in range(len(mensagem_original)):
        if mensagem_original[i] != mensagem_decripitada[i]:
            return "Mensagens diferentes"
    print("Mensagem decriptada corretamente")
               
# Programa Principal
letras = ascii_uppercase
outros = digits + punctuation + whitespace
outra_mensagem = "s"

while("s"):
    # conversor = {'8': '8', 'C': 'e', 'Y': 'n', 'U': 'x', 'G': 'u', 'Q': 'j', '^': '^', "'": "'", '~':
    # '~', 'Z': 'm', '/': '/', 'R': 'k', '+': '+', 'E': 't', 'D': 'r', '|': '|', 'K': 'a', '1': '1',
    # '?': '?', 'O': 'g', '\x0b': '\x0b', 'I': 'o', '4': '4', '(': '(', 'A': 'q', '.': '.', '{': '{',
    # '!': '!', '\r': '\r', ']': ']', '0': '0', '-': '-', 'B': 'w', '}': '}', '$': '$', 'S': 'l', 'W':
    # 'v', 'V': 'c', 'F': 'y', '7': '7', ';': ';', ' ': ' ', '*': '*', ')': ')', '%': '%', '#': '#',
    # '9': '9', '@': '@', '6': '6', '>': '>', '\\': '\\', '=': '=', '\x0c': '\x0c', 'H': 'i', 'M': 'd',
    # 'J': 'p', ',': ',', '<': '<', 'L': 's', '5': '5', 'P': 'h', 'X': 'b', '\t': '\t', '&': '&', '`':
    # '`', ':': ':', 'N': 'f', '\n': '\n', '_': '_', '3': '3', '[': '[', '2': '2', 'T': 'z', '"': '"'}

    # frase_original = """PREPAREM-SE PARA A ENCRENCA!
    # ENCRENCA EM DOBRO!
    # PARA PROTEGER O MUNDO DA DEVASTACAO!
    # PARA UNIR AS PESSOAS DE NOSSA NACAO!
    # PARA DENUNCIAR OS MALES DA VERDADE E DO AMOR!
    # PARA ESTENDER O NOSSO PODER AS ESTRELAS!
    # JESSE!
    # JAMES!
    # EQUIPE ROCKET DECOLANDO NA VELOCIDADE DA LUZ!
    # RENDA-SE AGORA OU PREPAREM-SE
    # PARA LUTAR!"""

    conversor = novos_caracteres()

    frase_original = input("Digite a frase que deseja encriptar: ").upper()

    mensagem_encripitada = encriptacao(frase_original, conversor)

    mensagem_decriptada = decriptacao(mensagem_encripitada, conversor)

    imprimir(frase_original, mensagem_encripitada, mensagem_decriptada)

    # verificacao(frase_original, mensagem_decriptada) # Descomente para verificar se a mensagem foi decriptada corretamente

    outra_mensagem = input("Deseja encriptar mais alguma mensagem? (s/n): ").lower()
    system("cls")

