"""Data Types"""

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

"""Mathematical Operation in Python"""

3 + 5
7 - 4
3 * 2
6 / 3
2 ** 3

# Ordem de Prioridade -> PEMDAS
# 1 - Parentheses -> ()
# 2 - Exponents -> **
# 3 - Mutiplication -> *
# 3 - Division -> /
# 4 - Addition -> +
# 4 - Subtraction -> -

print(3 * 3 + 3 / 3 - 3)

"""Number Manipulation and F Strings in Python"""

print(8/3)
print(int(8/3))
print(round(8/3, 2))
print(8//3)
print(type(8//3))
print(type(8/3))

results = 4/2
results /=2
print(results)

score = 0
height = 1.8
isWinning = True
# User scores a point
score += 1
print("your score is " + str(score))

#f-SyntaxWarning
print(f"your score is {score}, your height is {height}, your are winning is {isWinning}")