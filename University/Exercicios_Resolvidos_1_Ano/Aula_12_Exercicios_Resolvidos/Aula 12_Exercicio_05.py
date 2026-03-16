# Programa principal
s1 = input("Digite a primeira frase: ").lower()
s2 = input("Digite a segunda frase: ").lower()

jáFoi = ""
for letra in s1:
    if letra in s2 and letra not in " ,.;:!?" and letra not in jáFoi:
        print("A letra '%s' está na frase 2." %letra)
        jáFoi += letra
