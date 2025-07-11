import smtplib
from datamanage import DataManager
from flightsearch import FlightFinder
from notification_manager import NotificationManager
data_manager = DataManager()
flight_finder = FlightFinder()
data_manager.getData()
data_manager.get_user()
updated_row = flight_finder.find_iataCode(data_manager.data_rows)
data_manager.update_data_iataCode(updated_row)
cheap_flights = flight_finder.cheap_flight(updated_row)
notification_manager = NotificationManager()
notification_manager.send_email(data_manager.user_rows,cheap_flights)