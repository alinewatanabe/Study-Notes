"""Functions"""
def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")

#greet()

"""Functions with Inputs"""
def greet_with_name (name):
    print(f"Hello {name}")
    print("How do you do %s" %name)

#greet_with_name("Aline")

"""Functions with more than 1 input"""
def greet_with(name, location):
    print(f"Hello {name}")
    print("What is it like in %s?" %location)

#greet_with("Aline", "Sao Paulo")
#greet_with("Sao Paulo", "Aline")

"""Functions with Keywords Arguments"""
greet_with(location = "Sao Paulo", name = "Aline")