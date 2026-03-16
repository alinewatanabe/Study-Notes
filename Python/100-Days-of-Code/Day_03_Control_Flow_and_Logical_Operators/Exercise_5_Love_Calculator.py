print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name_1 = name1.lower()
name_2 = name2.lower()

t = name_1.count("t") + name_2.count("t")
r = name_1.count("r") + name_2.count("r")
u = name_1.count("u") + name_2.count("u")
e = name_1.count("e") + name_2.count("e")
digit_1 = str(t + r + u + e)

l = name_1.count("l") + name_2.count("l")
o = name_1.count("o") + name_2.count("o")
v = name_1.count("v") + name_2.count("v")
e = name_1.count("e") + name_2.count("e")
digit_2 = str(l + o + v + e)

score = int(digit_1 + digit_2)

if((score < 10) or (score > 90)):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif((score >= 40) and (score <= 50)):
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")