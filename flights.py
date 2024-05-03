from FlightRadar24 import FlightRadar24API
import pandas as pd
from datetime import datetime


fr_api = FlightRadar24API()  #create an instance of FlightRadar24API  

flights = fr_api.get_flights()  #Returns a list of Flight objects
flight=flights[0]
print(dir(flight))

columns_flights=['date_time','aircraft_code', 'airline_iata', 'airline_icao', 'altitude', 'callsign', 'destination_airport_iata', 'ground_speed', 'heading', 'icao_24bit', 'id', 'latitude', 'longitude', 'number', 'on_ground', 'origin_airport_iata', 'registration', 'squawk', 'time', 'vertical_speed']
df_flights= pd.DataFrame(columns=columns_flights)

for flight in flights: 
    df_flights.loc[len(df_flights)]= [datetime.now(),flight.aircraft_code, flight.airline_iata, flight.airline_icao, flight.altitude, flight.callsign, flight.destination_airport_iata, flight.ground_speed, flight.heading, flight.icao_24bit, flight.id, flight.latitude, flight.longitude, flight.number, flight.on_ground, flight.origin_airport_iata, flight.registration, flight.squawk, flight.time, flight.vertical_speed]

df_flights.to_csv("flights.csv",mode='a',index=False)
print(df_flights)

