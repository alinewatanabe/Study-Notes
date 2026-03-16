from Project_Art import logo, vs
from Game_Data import data
from os import system
import random
import time

def create_person(lista):
    L = []
    dicio = random.choice(lista)
    name = dicio['name']
    L.append(name)
    description = dicio['description']
    L.append(description)
    country = dicio['country']
    L.append(country)
    followers = dicio['follower_count']
    L.append(followers)                
    return L

verification = True
score = 0

while(verification == True):
    system("cls")
    print(logo)

    followers_A = create_person(data)
    print(f"Compare A: {followers_A[0]}, a {followers_A[1]}, from {followers_A[2]}")

    print(vs)

    followers_B = create_person(data)
    if(followers_B[0] == followers_A[0]):
        followers_B = create_person(data)
    print(f"Against B: {followers_B[0]}, a {followers_B[1]}, from {followers_B[2]}")

    ans = input("Who has more followers? Type 'A' or 'B': ").upper()

    if ((ans == 'A') and (followers_A[3] > followers_B[3])):
        score += 1
        print(f"You're right! Current score: {score}")
    elif((ans == 'B') and (followers_A[3] > followers_B[3])):
        print(f"Sorry, it's wrong.\n{followers_A[0]} has {followers_A[3]} followers, while {followers_B[0]} has {followers_B[3]} followers.")
        verification = False
    elif ((ans == 'B') and (followers_B[3] > followers_A[3])):
        score += 1
        print(f"You're right! Current score: {score}")
    elif((ans == 'A') and (followers_B[3] > followers_A[3])):
        print(f"Sorry, it's wrong.\n{followers_B[0]} has {followers_B[3]} followers, while {followers_A[0]} has {followers_A[3]} followers.")
        verification = False
    else:
        print("You may have write wrong. Please, try again")
    time.sleep(2)
        
print(f"Your scores is {score}")