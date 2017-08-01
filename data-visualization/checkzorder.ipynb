import os
import folium
print(folium.__version__)
import pandas as pd


state_geo = os.path.join('data', 'us-states.json')
state_unemployment = os.path.join('data', 'US_Unemployment_Oct2012.csv')

state_data = pd.read_csv(state_unemployment)

m = folium.Map(location=[48, -102], zoom_start=3, tiles='Stamen Toner')
m.choropleth(
    geo_path=state_geo,
    data=state_data,
    columns=['State', 'Unemployment'],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Unemployment Rate (%)'
)


popup = 'Must be on top of the choropleth'

m.add_child(folium.CircleMarker(location=[48, -102], radius=10, popup=popup))

m.save(os.path.join('results', 'CheckZorder.html'))

m
