""" FileNotFound
with open("file.txt") as file:
    file.read()

 KeyError
a_dictionary = {"key": "value"}
value = a_dictionarary["non_existent_key"]

 IndexError
fruit_list = ["Apple", "Banana", "Pear"]
fruit = fruit_list[3]

TypeError
text = "abc"
print(text + 5)"""

"""try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_massage:
    print(f"The key {error_massage} does not exist.")
else:
    content = file.read()
    print(content)
finally:    
    raise TypeError("This is an error that I made up")"""

height = float(input("Height: "))
weigth = int(input("Weight: "))

bmi = weigth/height**2
print(bmi)

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")