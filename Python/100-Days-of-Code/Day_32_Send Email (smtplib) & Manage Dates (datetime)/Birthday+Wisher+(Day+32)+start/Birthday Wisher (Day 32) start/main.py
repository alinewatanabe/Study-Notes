import smtplib
import datetime as dt
from random import choice

Monday = 0
Tuesday = 1
Wednesday = 2
Thursday = 3
Friday = 4
Saturday = 5
Sunday = 6

MY_EMAIL = "email.test.day32@gmail.com"
MY_PASSWORD = "ymqbtexhewynnhtz"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == Sunday:
    print(weekday)
    with open("quotes.txt") as data:
        all_quotes = data.readlines()
        quote = choice(all_quotes)

    with smtplib.SMTP("stmp@gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Random Quote\n\nYour random quote of day is:\n{quote}"
        )
