import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

legth = len(names)
select = random.randint(0, legth - 1)

person = names[select]
print("%s is going to buy the meal today!" %person)