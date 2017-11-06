import pandas as pd
import matplotlib.pyplot as plt

unrate = pd.read_csv('unrate.csv')
unrate['DATE'] = pd.to_datetime(unrate['DATE']) #将字符串类型的日期转换成严格意义上的pd.datetime类型

first_12 = unrate[:12]
plt.xticks(rotation = 90)
plt.xlabel('Month')
plt.ylabel('Unemployment Rate')
plt.title('Monthly Unemployment Trends, 1948')
plt.plot(first_12['DATE'],first_12['VALUE'])
plt.show()
