from email.message import EmailMessage
import smtplib
from config import EMAIL_FROM, EMAIL_PASSWORD, EMAIL_TO

class Weather_Notifier():

    def __init__(self):
        self.from_email = EMAIL_FROM
        self.to_email = EMAIL_TO
        self.password = EMAIL_PASSWORD
    # Send Email 
    def send_email(self,subject,body):
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.from_email
        msg['To'] = self.to_email
        msg.set_content(body)

        with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
            smtp.login(self.from_email,self.password)
            smtp.send_message(msg)

    # Trial email
    def trial_email(self):
        self.send_email(subject='Trial email',body='Hello, this is just a trial email')

notifier = Weather_Notifier()
notifier.trial_email()

