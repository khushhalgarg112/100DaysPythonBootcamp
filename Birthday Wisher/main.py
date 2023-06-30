import smtplib
import datetime as dt
import random
import pandas as pd

my_mail = "khusgarg1@gmail.com"
passwords = "whoctfqvshlsoggp"

my_mail = "khusgarg1@gmail.com"
password = "cykaddfeqswxekvz"

time = dt.datetime.now()

with open("quotes.txt") as quotes:
    quote_list = quotes.readlines()
    quote = random.choice(quote_list)

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_mail, password=password)
    connection.sendmail(
        from_addr=my_mail,
        to_addrs="khusgarg2002@gmail.com",
        msg=f"Subject: Today Motivation\n\n {quote}",
    )


"""date = dt.datetime.now()
today_tuple = (date.month, date.day)
birthday_list = pd.read_csv("birthday.csv")
birthday_list_dic = {
    (data_rows.month, data_rows.day): data_rows
    for (index, data_rows) in birthday_list.iterrows()
}

if today_tuple in birthday_list_dic:
    birthday_person = birthday_list_dic[today_tuple]
    with open("wish.txt", mode="r") as wish:
        con = wish.read()
        new_con = con.replace("[Name]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_mail, password=passwords)
        connection.sendmail(
            from_addr=my_mail,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday \n\n {new_con}",
        )
"""


# Sending mail
"""import smtplib

my_mail = "khusgarg1@gmail.com"
password = "ykdhgcrnwlysfurj"

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_mail, password=password)
    connection.sendmail(
        from_addr=my_mail,
        to_addrs="khusgarg2002@gmail.com",
        msg="Subject: Greet\n\n Hello Bro",
    )
"""

# Using datetime module
"""
import datetime as dt

time = dt.datetime.now()
year = time.year
print(year)

default_time = dt.datetime(year=2003, month=5,day=21)
print(default_time)"""
