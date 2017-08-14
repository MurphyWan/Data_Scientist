from foundmap import fmap
import pandas as pd
from pandas.io.json import json_normalize
import sys 
import json
import folium

geo_province = json.load(open('gj-china.json'))
data_province = json_normalize(geo_province['features'])
#data_province

dp = pd.DataFrame(data_province,
                  columns= ['id','properties.NAME', 'properties.ADCODE99'])

dp.rename(columns= {'id':'province_id','properties.NAME':'province', 'properties.ADCODE99':'ZIP_Code'}, inplace = True)
#print(data_province['properties.id', 'properties.name'])
dp.to_csv('json_to_province.csv', encoding = 'GB18030')


traffic_data = pd.read_csv('okay_traffic.csv', encoding = 'GB18030') 
td_pd = pd.DataFrame(traffic_data)


tp_merge = pd.merge(td_pd, dp, on = 'province', how = 'left')
tp_merge.to_csv('tp_merge.csv', encoding = 'GB18030')

tp = pd.read_csv('tp_merge.csv', encoding = 'GB18030')
tp = pd.DataFrame(tp, columns = ['province_id_y', 'count', 'province'])
tp = tp.rename(columns = {'province_id_y': 'province_id'})

default_encoding = 'utf-8'     

if  sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
geo_json = 'gj-china.json'    
    
map_1= fmap(38.6169, 109.3359, 4)

map_1.choropleth(geo_path = geo_json,
                  data = tp,
                  columns = ['province_id', 'count'],
                  threshold_scale = [50, 500, 1500, 3000, 5000, 10000],
                  key_on = 'feature.id',                 #没有找到正确的json文件！  一天一夜，总算找到正确的了，在https://github.com/python-visualization/folium/tree/master/examples/data
                  #key_on = 'STATE',
                  fill_color = 'YlOrRd',
                  fill_opacity = 0.7,
                  line_opacity = 0.2,
                  legend_name = 'traffic_distribution',
                  reset = True) 

folium.LatLngPopup().add_to(map_1)

map_1.save('./BSX_Riskmap/BSX_choropleth_traffic.html')