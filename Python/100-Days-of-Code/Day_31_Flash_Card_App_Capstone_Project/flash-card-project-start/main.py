from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
card = {}
words = {}

try:
    db = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    words = original_data.to_dict(orient="records")
except NameError:
    original_data = pd.read_csv("data/french_words.csv")
    words = original_data.to_dict(orient="records")
else:
    words = db.to_dict(orient="records")



def new_random_word():
    global card
    global flip_timer
    window.after_cancel(flip_timer)
    card = choice(words)
    canvas.itemconfig(img, image=card_front)
    canvas.itemconfig(country, text="French", fill=BACKGROUND_COLOR)
    canvas.itemconfig(word, text=card["French"], fill=BACKGROUND_COLOR)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(img, image=card_back)
    canvas.itemconfig(country, text="English", fill="white")
    canvas.itemconfig(word, text=card["English"], fill="white")

def is_known():
    words.remove(card)
    data = pd.DataFrame(words)
    data.to_csv("data/words_to_learn")
    new_random_word()


# ---------------------------------- UI -------------------------------- #
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.minsize(width=850, height=726)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_back = PhotoImage("images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
img = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
country = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, command=new_random_word)
wrong_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, command=is_known)
right_button.config(bg=BACKGROUND_COLOR, highlightthickness=0)
right_button.grid(row=1, column=1)

new_random_word()

window.mainloop()
