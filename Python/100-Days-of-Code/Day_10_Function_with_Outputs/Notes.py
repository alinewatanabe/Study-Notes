"""Functions with Output"""

def my_function(): 
    return 3 * 2 # Output = 6

def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return print("You didn't provide valid inputs.")
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    print(f"{formated_f_name} {formated_l_name}")

format_name(input("What's your first name? "), input("What is your last name? "))
