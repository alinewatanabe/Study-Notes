print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
porcent = float(input("What porcentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tax = (1 + porcent/100)
person_pay = (bill/people)*tax
final_amount = "{:.2f}".format(person_pay)
print(f"Each person should pay: ${final_amount}")