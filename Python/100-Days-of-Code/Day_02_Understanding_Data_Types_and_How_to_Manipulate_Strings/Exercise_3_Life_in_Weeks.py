age = input("What is your current age? ")

last_years = 90 - int(age)
days = 365*last_years
weeks = 52*last_years
months = 12*last_years

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
