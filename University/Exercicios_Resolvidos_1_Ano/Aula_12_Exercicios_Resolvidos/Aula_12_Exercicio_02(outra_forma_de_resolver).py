# Definição das funções
def contaVogais(frase):
    """retorna a quantidade de vogais da frase"""
    vogais = 0
    for letra in "aeiouáàãäâéèëêíìïîóòöõôúùüû":
        vogais += frase.count(letra)
    return vogais

# Programa principal
frase = input("Digite uma frase: ").lower()

print("A frase possui %i vogais." %contaVogais(frase))
