import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_reminder(): 
    sender_email = "dollochrisdavid@gmail.com"
    receiver_email = "cdollo1@umbc.edu"
    app_password = "avso ftur didn ybyr"

    subject = "Daily Reminder"
    body = "Hey! This is your daily reminder to set your heart ablaze ❤️‍🔥"
    message = f"Subject: {subject} \n\n{body}"

    #     since emojis are outside of the AsCII range and are unicode characters, the sendemail functions fails to encode the emoji
    #     as a fix we send our message as a MIME email with UTF-8 encoding
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, "plain", "utf-8"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()

def lambda_handler(event, context):
    send_daily_email()



