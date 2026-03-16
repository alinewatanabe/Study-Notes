################### Scope ####################

enemies = 1

def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


# Local Scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)

drink_potion()
# print(potion_strength) # NameError

# Global Scope
player_health = 10

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()
# There is no Block Scope
game_leve = 3
enemies = ["Skaleton", "Zombie", "Alien"]

if game_leve < 5:
    new_enemy = enemies[0]

print(new_enemy)

def create_enemy(game_leve, enemies):
    if game_leve < 5:
        new_enemy = enemies[0]
        print(new_enemy)

print(new_enemy) #Error

# Global Constants

PI = 3.141592
URL = "https://github.com/alinewatanabe"



