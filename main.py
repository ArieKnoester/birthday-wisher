import os
import smtplib
import datetime as dt
import pandas
import random
HOST_EMAIL = ""  # Ex. smtp.gmail.com, smtp.mail.yahoo.com
FROM_ADDR = ""  # email address to send from.
FROM_ADDR_APP_PASSWORD = ""  # 'App Password' for the FROM_ADDR account.
MY_NAME = ""  # Your first name or full name

# Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
this_month = now.month
today = now.day

birthdays_df = pandas.read_csv("birthdays.csv")
birthdays_today = birthdays_df.loc[
    (birthdays_df["month"] == this_month)
    & (birthdays_df["day"] == today)
]

# If there are birthdays today, pick a random template and email them.
if not birthdays_today.empty:
    birthdays_list = birthdays_today.to_dict(orient="records")
    for row in birthdays_list:
        name = row["name"]
        to_addr = row["email"]
        template = random.choice(os.listdir("letter_templates"))
        with open(f"letter_templates/{template}") as file:
            email_body_text = file.read().replace("[NAME]", name).replace("[MY_NAME]", MY_NAME)
        with smtplib.SMTP(HOST_EMAIL) as connection:
            connection.starttls()
            connection.login(user=FROM_ADDR, password=FROM_ADDR_APP_PASSWORD)
            connection.sendmail(
                from_addr=FROM_ADDR,
                to_addrs=to_addr,
                msg=f"Subject: Happy Birthday!\r\n{email_body_text}"
            )
