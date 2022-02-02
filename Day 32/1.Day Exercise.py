# import smtplib
#
# my_email = "abc@gmail.com"        # Enter Your Email
# password = "*********"            # Enter Your Password
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, to_addrs="dasrajdip@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )

############################################################

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=2001, month=8, day=30, hour=4)
print(date_of_birth)
