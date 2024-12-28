import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()
hour = now.hour
print(now)

sender_email = "bedobenedek5@gmail.com"
sender_password = "qjqi mtxw gjqp kyot"
recipient_email = "bedo1benedek@gmail.com"

if hour == 8:
    with open("quotes.txt", "r") as file:
        content = file.readlines()
        random_quote = random.choice(content)

    # Send email using SMTP
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_password)
        connection.sendmail(
        from_addr=sender_email, 
        to_addrs=recipient_email,
        msg=f"Subject:Be a Superhuman today!\n\n {random_quote}"
    )