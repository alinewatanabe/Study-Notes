import os
import Art_Project as art

other_bidders = True
bids = {}

while (other_bidders):
    print(art.logo)
    print("Welcome to the secret auction program.")
    name = input("What is your name? ").title()
    bid = int(input("What's your bid? $"))
    bids[name] = bid
    other_bidders = input("Are ther any other bidders? Type 'yes' or 'no'\n").lower()
    if (other_bidders == "no"):
        other_bidders = False
    os.system("cls")

highest_bid = 0

for name in bids:
    if (bids[name] > highest_bid):
        highest_bid = bids[name]
        person = name

print(f"The winner is {person} with a bid of ${highest_bid}.")