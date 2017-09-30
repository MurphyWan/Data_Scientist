## 2. Introduction to the Data ##

'''
## 这节讲 pd.read_csv()读取两个文件，并显示前五行，非常简单。

'''

import pandas as pd

all_ages = pd.read_csv('all-ages.csv')
recent_grads = pd.read_csv('recent-grads.csv')
all_ages[:5]
recent_grads[:5]

