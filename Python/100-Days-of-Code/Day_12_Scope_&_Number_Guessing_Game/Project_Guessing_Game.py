import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1,100)
# print(number)


difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if (difficulty == 'easy'):
    attempts = 10
else:
    attempts = 5

while(attempts > 0):
    print(f"You have {attempts} attempts remainig to guess the number.")
    guess = int(input("Make a guess: "))
    if(guess > number):
        print("Too high")
        print("Guess again.")
    elif(guess < number):
        print("Too low")
        print("Guess again")
    elif(guess == number):
        print("You got it")
        break
    attempts -= 1

if(attempts == 0):
        print("You not have more attempts")
        print(f"Your number was {number}")
        print("Game Over")