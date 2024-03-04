# import smtplib
# from multiprocessing import connection
#
# my_email = "adityam874@gmail.com"
# password = "khiladi786"
#
# """
# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()
# connection.login(user=my_email, password=password)
# connection.sendmail(
#     from_addr=my_email,
#     to_addrs="adityamsr03@gmail.com",
#     msg="Subject:Hello\n\nThis is the body of my email."
# )
# connection.close()
#
# """
#
# with smtplib.SMTP("smtp.gmail.com") as connnection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="adityamsr03@gmail.com",
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )
# connection.close()

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
if year == 2023:
    print("wear a face mask")
print(now)
print(year)
print(day_of_week)

date_of_birth = dt.datetime(year=2003, month=8, day=12, hour=12)
print(date_of_birth)