from FlightRadar24 import FlightRadar24API
import pandas as pd

fr_api = FlightRadar24API()  #create an instance of FlightRadar24API
airports = fr_api.get_airports()  # Returns a list of Airport objects
print(dir(airports[0]))   #get the airports object atributes

columns_airports=['altitude', 'country', 'get_distance_from', 'iata', 'icao', 'latitude', 'longitude', 'name', 'set_airport_details']
df_airports= pd.DataFrame(columns=columns_airports)

for airport in airports: 
    df_airports.loc[len(df_airports)]= [airport.altitude, airport.country, airport.get_distance_from, airport.iata, airport.icao, airport.latitude, airport.longitude, airport.name, airport.set_airport_details]

df_airports.to_csv("airports.csv")

print(df_airports)