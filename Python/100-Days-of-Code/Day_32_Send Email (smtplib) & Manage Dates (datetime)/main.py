import smtplib
import datetime as dt
from random import choice

my_email = "email.test.day32@gmail.com"
password = "htihhmojxcrfycot"

"""gmail = "smtp.gmail.com"
hotmail = "stmp.live.com"
outlook = "outlook.office365.com"
yahoo = "stmp.mail.yahoo.com"""

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="emailtestday32@yahoo.com",
        msg="Subject:Hello\n\nThis is the body of my email"
    )


'''
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=2023, month=8, day=25, hour=15)
print(date_of_birth)'''