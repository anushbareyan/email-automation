import os
import random
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import time
import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
os.chdir("for_email_auto")

# SMTP server config
smtp_server = "smtp.gmail.com"
port = 465
sender_email = "email@gmail.com"
password = "pass"

# create message components
subject = ""
recipients_list = []

# number of emails to send from the list
num_emails = 84 
with open('your_data.txt', 'r') as file:
    for i, line in enumerate(file):
        if i == num_emails:
            break
        email = line.strip()
        recipients_list.append(email)

# HTML body
body = MIMEText(
    f"""\
    <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        </head>
        <body>
            <p>Some information</p>
        </body>
    </html>
    """, _subtype="html", _charset='utf-8'
)

i = 0
for recipient in recipients_list:
    # for each email connect to the SMTP server and send emails, this is done so that the email is sent to each one individually and doesn't conatain other email in To field
    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.login(sender_email, password)
        msg = MIMEMultipart()

        msg['To'] = recipient
        msg['Subject'] = subject
        msg["From"] = formataddr(("Your name", f"{sender_email}"))
        msg["BCC"] = "email@gmail.com"

        with open("entuziast.jpg", "rb") as f:
            img_data = f.read()

        msg.attach(body)
        photo_filename = 'someimage.jpg'
        with open(photo_filename, 'rb') as attachment:
            photo_part = MIMEBase('application', 'octet-stream')
            photo_part.set_payload(attachment.read())
            encoders.encode_base64(photo_part)
            photo_part.add_header('Content-Disposition',
                                  f'attachment; filename= {photo_filename}')
            msg.attach(photo_part)

        try:
            server.sendmail(sender_email, recipient, msg.as_string())
            i += 1
            print(f"{i} successfully sent: {recipient}")
            with open('log.txt', 'a') as file:
                file.write(f"successfully sent: {recipient}\n") # creates a file log.txt and adds log about the status
        except Exception as e:
            i += 1
            print(f"{i} failed to send: {recipient}")
            with open('log.txt', 'a') as file:
                file.write(f"failed to send: {recipient}\n")
        del msg['Content-Type']
        del msg['Content-Disposition']
        del msg['MIME-Version']
        server.quit()
        time.sleep(120 * (random.uniform(0, 1.5) + 1)) #this is done because of Gmail restrictions to send some amount of emails per day. Sending all at once will get your email marked as spam
