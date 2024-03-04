import datetime as dt
import smtplib
import random

my_email = "adityam874@gmail.com"
password = "khiladi786"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="adityamsr03@gmail.com",
            msg=f"Subject:Monday motivation\n\n{quote}"
        )

