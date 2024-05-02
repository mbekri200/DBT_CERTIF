from FlightRadar24 import FlightRadar24API
import pandas as pd

fr_api = FlightRadar24API()  #create an instance of FlightRadar24API  

zones = fr_api.get_zones()  #Returns a list of Flight objects
main_zones=zones.keys()


columns_zones= ['zone_name','tl_y', 'tl_x', 'br_y', 'br_x', 'subzones']
df_zones= pd.DataFrame(columns=columns_zones)

for zone_name in zones: 
    zone=zones[zone_name]
    if 'subzones' in zone.keys():
        df_zones.loc[len(df_zones)]= [zone_name,zone['tl_y'], zone['tl_x'], zone['br_y'], zone['br_x'], zone['subzones']]
    else:
        df_zones.loc[len(df_zones)]= [zone_name,zone['tl_y'], zone['tl_x'], zone['br_y'], zone['br_x'], 'null']

df_zones.to_csv('zones.csv',index=False)