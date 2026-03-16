import random
import os
from Hangman_art import logo, stages
from Hangman_words import word_list

print(logo)

word = random.choice(word_list)
word_length = len(word)

#print(f"\nThe answer is: {word}")

display = []
tried = []
end_of_game = False
lives = 6

for _ in range(word_length):
    display += "_"

while (not end_of_game):
    print(stages[lives])
    print(f"You already tried: {', '.join(tried)}")
    guess = input("\nGuess a letter: ").lower()
    if guess not in tried:
        tried.append(guess)
        tried.sort()

    os.system("cls")
    
    if (guess in display):
        print("You already guess the letter.\n")
    
    for position in range(word_length):
        letter = word[position]
        if(letter == guess):
            display[position] = letter
            
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You win!")

    if guess not in word:
        print(f"\nYou guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

    if lives < 0:
        end_of_game = True
        print(f"You lose.\nThe word was {word}.")