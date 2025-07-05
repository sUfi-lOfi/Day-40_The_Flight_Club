import os

from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv("./variable.env")
class NotificationManager:
    def __init__(self):
        self.id = os.getenv("twilio_id")
        self.token = os.getenv("twilio_token")
        self.client = Client(self.id,self.token)
    def send_message(self,list):
        for flight in list:
            self.client.messages.create(
                body= f"Low price alert : {flight["price"]}£\nFrom : {flight["from"]}\nTo : {flight["to"]}",
                from_ = os.getenv("twilio_from_num"),
                to = os.getenv("twilio_to_num")
            )
