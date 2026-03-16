##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
from random import randint
import smtplib

my_email = "email.test.day32@gmail.com"
password = "htihhmojxcrfycot"

now = dt.datetime.now()
today = (now.month, now.day)

csv = pd.read_csv("birthdays.csv")

birthday_dict = {(csv_row["month"], csv_row["day"]): csv_row for (index, csv_row) in csv.items()}
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    file = f"letter_templates/letter_{randint(1,3)}.txt"
    with open(file) as letters:
        contents = letters.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{contents}"
        )

