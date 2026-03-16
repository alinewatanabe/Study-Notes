import random
import my_module

"""Generating Random Integers Numbers"""
# Essa função inclui o numero de inicio e fim. Nesse caso, o 1 e o 10.
random_integer = random.randint(1,10)

print(random_integer)

love_score = random.randint(1,100)
print(f"Your love score is {love_score}")


"""Creating Modules"""
print(my_module.pi)


"""Generating Random Floating Point Numbers"""
# Essa função inclui apenas o numero inicial, portanto nesse caso nunca tera a possibilidade de ter 1 como resposta

random_float = random.random() # Sempre gerara um numero entre 0 e 1

print(random_float)

random_float_5 = random_float * 5

print(random_float_5) # float que varia de 0 a 5


"""List"""
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[2])
print(states_of_america[-2])

states_of_america[1] = "Pencilvania"

states_of_america.append("End Island")

states_of_america.extend(["Teethless"])

print(states_of_america)

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]

vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)