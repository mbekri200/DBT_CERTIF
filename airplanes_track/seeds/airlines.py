from FlightRadar24 import FlightRadar24API
import pandas as pd

fr_api = FlightRadar24API()  #create an instance of FlightRadar24API  
airlines = fr_api.get_airlines()

airlines_cols=['Name', 'Code', 'ICAO']
df_airlines= pd.DataFrame(columns=airlines_cols)

for airline in airlines:
    df_airlines.loc[len(df_airlines)]= [airline['Name'], airline['Code'], airline['ICAO']]

df_airlines.to_csv('airlines.csv',index=False)

