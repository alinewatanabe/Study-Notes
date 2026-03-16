# Data Types

# Strings
print("Exemplos de Strings: ")
print("Hello"[4])
print("123" + "345")
print("hello","world\n")

#Integer
print("Exemplos de Integer: ")
print(123 + 345)
print(123_456) # O python ignora o _ e considera um numero inteiro, isso é usado apenas para ajudar o programador a se organizar quando for mexer com mil, milhoes, bilhoes
print(123_456 + 111)

# Float
print("\nExemplos de Float: ")
print(123.32)

#Boolean
True
False

num_char = len(input("What is your name?"))
new_num_char = str(num_char)

print("Your name has " + new_num_char + " characers")

a = float(123)
print(type(a))

print(70 + float("100.5"))
print(str(70) + str(100))