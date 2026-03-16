#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

Names_list = []

with open("./Input/Names/invited_names.txt") as names_file:
    Names_list_original = names_file.readlines()

    for names in Names_list_original:
        Names_list.append(names.strip())

with open("./Input/Letters/starting_letter.txt") as letters_file:
    Letter = letters_file.read()

    for name in Names_list:
        New_letter = Letter.replace("[name]", name)
        with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as letter_file:
            letter_file.write(New_letter)
