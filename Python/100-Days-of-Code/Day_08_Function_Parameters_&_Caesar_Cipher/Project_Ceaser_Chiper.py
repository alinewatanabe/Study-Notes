import os
import time
import Art_Project_Ceaser_Chiper as apcc

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser(direction, text, shift):
    txt = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if(direction == "encode"):
                new_position = position + shift
                Error = False
            elif(direction == "decode"):
                new_position = position - shift
                Error = False
            else:
                print("Error. Try Again")
                time.sleep(2)
                os.system("cls")
                Error = True
            new_letter = alphabet[new_position]
            txt += new_letter
        else:
            txt += letter
    print(f"The {direction}d text is {txt}")
    return Error


reply = True

while ((reply == True)):
    
    print(apcc.logo)    
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    shift = shift%26
    
    Error = ceaser(direction = direction, text = text, shift = shift)
    
    
    if(Error == False):    
        quest = input("Type 'yes if you want to go again. Otherside type 'no.\n").lower()
        
        if(quest == "yes"):
            reply = True
            os.system("cls")
        else:
            reply = False
            print("Ok! Thanks for using Ceaser Chiper :)")
    else:
        reply = True
        os.system("cls")