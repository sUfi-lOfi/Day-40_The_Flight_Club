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
        self.user_rows = None

    def getData(self):
        sheety_get_url = "https://api.sheety.co/4055e736c0604c3f090ffb10b2f4e279/theFlightClub/prices"
        sheety_request = requests.get(sheety_get_url,auth=self.authentication_header)
        self.data_rows = sheety_request.json()['prices']
    def update_data_iataCode(self,list):
        for row in list:
            sheet_edit_request = requests.put(
            f"https://api.sheety.co/4055e736c0604c3f090ffb10b2f4e279/theFlightClub/prices/{row['id']}",
            json={"price": row},
            auth=self.authentication_header
            )
    def get_user(self):
        sheety_get_url = "https://api.sheety.co/4055e736c0604c3f090ffb10b2f4e279/theFlightClub/formResponses1"
        sheety_request = requests.get(sheety_get_url, auth=self.authentication_header)
        self.user_rows = sheety_request.json()['formResponses1']
    def add_entry(self,fName,lName,email):
        entry= {
            "formResponses1" : {
                "firstName" : fName,
                "lastName" : lName,
                "email" : email
            }
        }
        sheety_post_url = "https://api.sheety.co/4055e736c0604c3f090ffb10b2f4e279/theFlightClub/formResponses1"
        sheety_post_data = requests.post(sheety_post_url,json=entry,auth=self.authentication_header)

