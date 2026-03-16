from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    passwords_letters = [choice(letters) for char in range(randint(8,10))]
    passwords_numbers = [choice(numbers) for c in range(randint(2,4))]
    passwords_symbols = [choice(symbols) for i in range(randint(2,4))]

    passwords_list = passwords_letters + passwords_symbols + passwords_numbers
    shuffle(passwords_list)

    password = "".join(passwords_list)

    if len(entry_password.get()) == 0:
        entry_password.insert(0, password)
    else:
        entry_password.delete(0, END)
        entry_password.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    email = entry_email_username.get()
    password = entry_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nis it ok to save?")

        if is_ok:
            with open("passwords.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")
            entry_password.delete(0, END)
            entry_website.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Label
label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

label_email_username = Label(text="Email/Username:")
label_email_username.grid(column=0, row=2)

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

# Button
button_generate = Button(text="Generate Password", command=generate_password)
button_generate.grid(row=3, column=2)

button_add = Button(text="Add", width=35, command=save)
button_add.grid(row=4, column=1, columnspan=2)

# Entries
entry_website = Entry(width=35)
entry_website.grid(row=1, column=1, columnspan=2)
entry_website.focus()

entry_email_username = Entry(width=35)
entry_email_username.insert(0, "aline@gmail.com")
entry_email_username.grid(row=2, column=1, columnspan=2)

entry_password = Entry()
entry_password.grid(row=3, column=1)


window.mainloop()