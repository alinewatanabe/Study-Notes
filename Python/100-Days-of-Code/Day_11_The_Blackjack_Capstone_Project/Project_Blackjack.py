import random
from os import system
from Art_Project import logo

def add_card(view_list, cards, user_list, symbol_cards):
    value_random = random.choice(cards)
    position = cards.index(value_random)
    user_list.append(value_random)
    view_list.append(symbol_cards[position])
    
def score(base_list):
    score = 0
    for number in base_list:
        score += number
    return score

def verification_list(symbols_list, score):
    for symbol in symbols_list:
        if (symbol == 'A'):
            if(score > 21):
                score -= 10
    return score
                
    
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
symbol_cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
user_list = []
view_user_list = []
computer_list = []
view_comp_list = []
another_card = 'y'

# Add Initial User Cards
add_card(view_user_list, cards, user_list, symbol_cards)
add_card(view_user_list, cards, user_list, symbol_cards)

# Add Initial Computer Cards
add_card(view_comp_list, cards, computer_list, symbol_cards)
add_card(view_comp_list, cards, computer_list, symbol_cards)

while(another_card == 'y'):
    print(logo)
    # Scores
    user_score = score(user_list)
    comp_score = score(computer_list)
        
    print(f"Your cards: {view_user_list}, current score: {user_score}")
        
    #print(f"Computer's cars: {view_comp_list}, current score: {comp_score}")
    print(f"Computer's first card: {view_comp_list[0]}")

    another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    if (another_card == 'y'):
        system("cls")
        add_card(view_user_list, cards, user_list, symbol_cards)

score_user = verification_list(view_user_list, user_score)
score_comp = verification_list(view_comp_list, comp_score)

print(f"Your final hand: {view_user_list}, final score: {score_user}")
print(f"Computer's final hand: {view_comp_list}, final score: {score_comp}")

if(score_user > 21 and score_comp > 21):
    print("Both lose")
elif((score_user > 21 and score_comp <= 21) or (score_user < score_comp)):
    print("You went over. You lose")
elif((score_user <= 21 and score_comp > 21) or (score_user > score_comp)):
    print("Congratulation! You win. :)")
else:
    print("Sorry, but it's draw")