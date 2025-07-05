import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
load_dotenv("./variable.env")

class DataManager:
    def __init__(self):
        self.username = os.getenv("sheety_user")
        self.passcode = os.getenv("sheety_pass")
        self.authentication_header = HTTPBasicAuth(username=self.username,password=self.passcode)
        self.data_rows = None

    def getData(self):
        sheety_get_url = "https://api.sheety.co/4f6a474e6880d516f282fc8a3c3495ca/copyOfFlightDeals/prices"
        sheety_auth = HTTPBasicAuth(username=os.getenv("sheety_user"),password=os.getenv("sheety_pass"))
        sheety_request = requests.get(sheety_get_url,auth=sheety_auth)
        self.data_rows = sheety_request.json()['prices']
    def update_data_iataCode(self,list):
        for row in list:
            sheet_edit_request = requests.put(
            f"https://api.sheety.co/4f6a474e6880d516f282fc8a3c3495ca/copyOfFlightDeals/prices/{row["id"]}",
            json={"price": row},
            auth=self.authentication_header
            )