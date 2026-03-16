from tkinter import *

def miles_to_km():
    miles_value = float(input_miles.get())
    km_value.config(text=str(round(miles_value*1.689, 2)))


window = Tk()
window.title("Mile to Km Converter")
window.minsize(height=160, width=300)
window.config(padx=30, pady=30)

# Label
miles = Label(text="Miles", font=("Arial", 14))
miles.grid(column=2, row=0)
km = Label(text="Km", font=("Arial", 14))
km.grid(column=2, row=1)
equal = Label(text="is equal to", font=("Arial", 14))
equal.grid(column=0, row=1)
km_value = Label(text="0", font=("Arial", 14))
km_value.grid(column=1, row=1)

# Entry
input_miles = Entry(width=15)
input_miles.grid(column=1, row=0)

# Button
calculate = Button(text="Calculate", font=("Arial", 14), command=miles_to_km)
calculate.grid(column=1, row=2)
window.mainloop()
