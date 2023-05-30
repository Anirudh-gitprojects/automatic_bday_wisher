##################### Extra Hard Starting Project ######################
import datetime as dt
import random
import smtplib
import csv
import pandas
now=dt.datetime.now()
year=now.year
days=now.day
month=now.month
this_date=(days,month)
print(this_date)
data=pandas.read_csv('birthdays.csv')
new_dict={(data_row['day'], data_row['month']): data_row for (index,data_row) in data.iterrows()}
print(new_dict)
if this_date in new_dict:
    bday_person=new_dict[this_date]
    with open(f"letter_{random.randint(1,3)}.txt") as file:
        contents= file.read()
        a=contents.replace("[NAME]",f"{bday_person['name']}")
        print(a)

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login("YOUR_EMAIL@gmail.com",password="[YOUR PASSKEY")
        connection.sendmail(from_addr="anismessages@gmail.com",to_addrs=f"{bday_person['email']}",msg=f"Subject:Happy Birthday!\n\n{a}")
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address



