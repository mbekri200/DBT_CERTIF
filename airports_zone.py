import pandas as pd

def coord_zones(latitude, longitude):
    
        df_zones=pd.read_csv('zones.csv')
        i=0
        while i < len(df_zones):
            br_x = df_zones['br_x'].iloc[i]
            br_y = df_zones['br_y'].iloc[i]
            tl_x= df_zones['tl_x'].iloc[i]
            tl_y= df_zones['tl_x'].iloc[i]
            if br_y <= latitude <= tl_y  and br_x <= latitude <= tl_x:
                return df_zones['zone_name'].iloc[i]
                break
            else :
                i=i+1




"""
def airport_zone():
    airports=pd.read_csv('airports.csv')
    airports_zone=airports.assign(zone=[coord_zones(airports['latitude'].iloc[i],airports['longitude'].iloc[i]) for i in range(len(airports))])
    print(airports_zone)
    airports_zone.to_csv('airports_zones.csv',index=False)
    return airports_zone

airport_zone()
"""









