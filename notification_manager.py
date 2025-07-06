import os
import smtplib
import random
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv("./variable.env")
class NotificationManager:
    def __init__(self):
        self.id = os.getenv("twilio_id")
        self.token = os.getenv("twilio_token")
        self.client = Client(self.id,self.token)
        self.my_email = os.getenv('my_email')
    def send_message(self,list):
        for flight in list:
            self.client.messages.create(
                body= f"Low price alert : {flight["price"]}£\nFrom : {flight["from"]}\nTo : {flight["to"]}",
                from_ = os.getenv("twilio_from_num"),
                to = os.getenv("twilio_to_num")
            )
    def send_email(self,user_list,cheap_flights):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=os.getenv("app_password"))
            for user in user_list:
                flight_suggestion = random.choice(cheap_flights)
                connection.sendmail(from_addr=self.my_email,to_addrs=user["email"],msg=f"Subject:Flight Found!!\n\nThe flight is going from {flight_suggestion["from"]} to {flight_suggestion["to"]} with the lowest price of {flight_suggestion["price"]}")
