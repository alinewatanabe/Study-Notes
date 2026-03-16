from Data_Base import resources, MENU
from os import system
from time import sleep


MONEY = 0

def check_resources(drink):
    """Check if the resourses are sufficient to make the drink"""
    for ingredient in MENU[drink]["ingredients"]:
        item = MENU[drink]["ingredients"][ingredient]
        resource = resources[ingredient]
        if(item <= resource):
            resources[ingredient] -= item
        else:
            print(f'Sorry but there is not enought {ingredient}')
            return False
        return True
    
def process_coin(drink):
    global MONEY
    price = MENU[drink]['cost']
    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickles = float(input("How many nickles? "))
    pennies = float(input("How many pennies? "))
    total = 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies
    if(total == price):
        print(f'Here is your {drink}. Enjoy!')
        MONEY += price
    elif(total > price):
        change = total - price
        print(f'Here is ${change:.2f} dollars in change. Enjoy your {drink}!')
        MONEY += price
    else:
        print("Sorry that's not enought money. Money refunded")
        
        
        
drink = "start"

while(drink != "off"):
    loop = True
    while(loop):
        sleep(4)
        system("cls")
        drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if(drink == "report"):
            print(f'Water: {resources["water"]} ml')
            print(f'Milk: {resources["milk"]} ml')
            print(f'Coffee: {resources["coffee"]} ml')
            print(f'Money: ${MONEY}')
        
        elif(drink == 'off'):
            break
        
        elif(drink == 'add'):
            ingredient = input("Which is the ingrendient to add (water/milk/coffee)? ").lower()
            value_append = float(input(f'How much of {ingredient} will be add? '))
            value = resources[ingredient]
            value += value_append
            resources[ingredient] = value

        else:
            if(check_resources(drink)):
                process_coin(drink)
                loop = False
            else:
                print("Sem recursos suficiente")
            