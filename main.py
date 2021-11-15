##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
# HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
import csv
import datetime
import random
import smtplib

list_q = []
with open("quotes.txt", encoding="utf8") as quotes:
    list_q = quotes.readlines()

date = datetime.datetime.now()

day_name = date.date().strftime("%A")


def send_mail(quote, name_to, day):
    server = smtplib.SMTP('smtp.telenet.be')
    server.set_debuglevel(1)
    server.sendmail("benoit.goethals@telenet.be", name_to, f"Subject: Hi there\n msg: {day}\n{quote}".encode("utf-8"))
    server.quit()


show = random.choice(list_q)
with open('birthdays.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    line_count = 0
    for row in csv_reader:
        if line_count > 0:
            send_mail(show,row[1], day_name)
        line_count += 1
    print(f'Processed {line_count} lines.')
