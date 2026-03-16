import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

while(choice < 0 or choice >= 3):
    print("You typed an invalid number, try again.")
    choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if(choice == 0):
    print(rock)
elif(choice == 1):
    print(paper)
else:
    print(scissors)

comp_choice = random.randint(0,2)

print("Computer chose:")
if(comp_choice == 0):
    print(rock)
elif(comp_choice == 1):
    print(paper)
else:
    print(scissors)

if((choice == 0) and (comp_choice == 2)):
    print("you win!")
elif((choice == 2) and (comp_choice == 0)):
    print("You lose")
elif(comp_choice > choice):
    print("You lose")
elif(choice > comp_choice):
    print("You win!")
else:
    print("It's a draw")

