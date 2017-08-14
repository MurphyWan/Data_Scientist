import foundmap
import folium
import pandas as pd

#foundation map
map_18 = foundmap.fmap(31.2250, 121.4648, 6)

marker_cluster = folium.MarkerCluster().add_to(map_18)

records_limit = 1000

# for row in traffic_data[0:records_limit].iterrows():
#      map_18.Marker(
#          location = [row[1]['Y'],row[1]['X']], 
#          clustered_marker = True)
#Marker(location=[45.5, -122.3], popup=folium.Popup('Portland, OR'))

traffic_data = pd.read_csv('02-new_traffic.csv',encoding = 'GB18030' )
traffic_data.head()

for row in traffic_data[0:records_limit].iterrows():
    folium.Marker(
        location = [row[1]['Y'],row[1]['X']],
        popup=folium.Popup(row[1]['province']+row[1]['city']+row[1]['area']),
        icon=folium.Icon(color='orange', icon='stop-sign'),
                 ).add_to(marker_cluster)       

        
        
        
map_18.save('./BSX_Riskmap/BSX_dscatter_traffic.html')    