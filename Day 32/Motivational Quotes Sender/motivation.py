import smtplib
import datetime as dt
import random

MY_EMAIL = "abc@gmail.com"      # Enter Your Email
MY_PASSWORD = "********"        # Enter Your Password

now = dt.datetime.now()
weekday = now.weekday()
day_name = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for day in range(0, 7):
    if weekday == day:
        with open("quotes.txt") as quote_file:
            all_quotes = quote_file.readlines()
            quote = random.choice(all_quotes)

        print(quote)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="dasrajdip@gmail.com",
                msg=f"Subject:{day_name[day]} Motivation\n\n{quote}"
            )
