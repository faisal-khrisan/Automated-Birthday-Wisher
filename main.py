import pandas as pd
import smtplib
import random
import datetime as dt

EMAIL = "example@gmail.com"
PASSWORD = "Your app password"

# Organise the data
data = pd.read_csv("birthdays.csv")
recode_data = data.to_dict(orient="records")

# check the birthday of the person
current_date = dt.datetime.now()
current_month = current_date.month
current_day = current_date.day

# Organise the letters
letters = ["letter_1.txt", "letter_2.txt","letter_3.txt","letter_4.txt","letter_5.txt"]



#  Check if today matches a birthday in the birthdays.csv
# Send the letter generated  to that person's email address.
for item in recode_data :
    if current_month == item["month"]:
        if current_day == item["day"]:
            with open(f"letter_templates/{random.choice(letters)}", "r", encoding="utf-8") as file:
                content = file.read()
            wishes_message = content.replace("[Name]", item["name"])
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=EMAIL, password=PASSWORD)
                connection.sendmail(from_addr=EMAIL, to_addrs=item["email"], msg=wishes_message.encode("utf-8"))










