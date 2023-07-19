from twilio.rest import Client
import smtplib

MAIL_TOKEN = "lsfndladshiiavmo"
MY_MAIL = "khusgarg1@gmail.com"


class NotificationManager:
    def __init__(self):
        pass

    def send_mail(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_MAIL, password=MAIL_TOKEN)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_MAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode("utf-8"),
                )
