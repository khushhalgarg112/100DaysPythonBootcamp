from twilio.rest import Client
import smtplib


ACC_SID = "AC47f7d48de5d76ea50f#f0765acbaf333f"
API_KEY = "4ce91d0bc63a01f15cb2#9fe17ef564b9"
TWILIO_NUM = "+14178#554309"
PERSONAL_NUMBER = "+918307191801"

MAIL_TOKEN = "lsfndla#dshiiavmo"
MY_MAIL = "khusgarg1@gmail.com"

class NotificationManager:
    
    def __init__(self) :
        self.client = Client(ACC_SID, API_KEY)

    def send_message(self, message):
        message = self.client.messages.create(body=message, from_=TWILIO_NUM, to=PERSONAL_NUMBER,)
        print(message.status)


    def send_mail(self,emails, message):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_MAIL, password=MAIL_TOKEN)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_MAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
