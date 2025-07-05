import os
import requests
from dotenv import load_dotenv
import datetime
load_dotenv("./variable.env")

class FlightFinder:
    def __init__(self):
        self.api_key = os.getenv("flight_api_key")
        self.api_secret = os.getenv("flight_api_secret")
        flight_token_header = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
        flight_token_body = {
            "grant_type": "client_credentials",
            "client_id": self.api_key,
            "client_secret": self.api_secret
        }
        flight_token_url = "https://test.api.amadeus.com/v1/security/oauth2/token"
        flight_token_request = requests.post(flight_token_url, data=flight_token_body, headers=flight_token_header)
        self.api_token  = flight_token_request.json()["access_token"]
        self.authorization_header = dict(Authorization=f"Bearer {self.api_token}")


    def find_iataCode(self,list):
        flight_code_url = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        for n,city in enumerate(list):
            flight_code_params = {
                "keyword": city["city"],
            }
            flight_code_request = requests.get(flight_code_url,params=flight_code_params,headers=self.authorization_header)
            list[n]["iataCode"] = flight_code_request.json()['data'][0]["iataCode"]
        return list


    def cheap_flight(self,list):
        tomorrow_date = datetime.datetime.now()
        tomorrow_date = tomorrow_date.replace(day=tomorrow_date.day + 1)
        tomorrow_date = tomorrow_date.strftime("%Y-%m-%d")
        cheap_flight_list = []
        flight_price_url = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        for row in list:
            print(f"Printing Price for {row["city"]}")
            flight_price_params = {
            "originLocationCode" : "LON",
            "destinationLocationCode" : row["iataCode"],
            "departureDate" : tomorrow_date,
            "adults" : 1,
            'maxPrice': int(row["lowestPrice"]),
            "currencyCode":"GBP"
            }
            flight_price_request = requests.get(flight_price_url,params=flight_price_params,headers=self.authorization_header)
            flight_price_data = flight_price_request.json()
            if len(flight_price_data["data"]) == 0:
                pass
            else:
                flight_prices = [float(price["price"]["total"]) for price in flight_price_data["data"] ]
                lowest_price = min(flight_prices)
                for flight in flight_price_data["data"]:
                    if float(flight["price"]["total"]) == lowest_price:
                        flight_data = {
                            "price" : lowest_price,
                            "from" :flight["itineraries"][0]["segments"][0]["departure"]["iataCode"],
                            "to" : flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
                        }
                        cheap_flight_list.append(flight_data)
                        break
        return cheap_flight_list

