## 1. Data Structures ##

'''
## 这节讲 Pandas的Series基本功能
## 以及讲 以FivethirtyEight提供的数据为基础，读取文件并前两行。

'''

import pandas as pd

fandango = pd.read_csv('fandango_score_comparison.csv')
print(fandango.head(2))

## 2. Integer Indexes ##

'''
## 这节讲 选择DF中的两个列。so easy！

DF用Series来表示列。当我们从DF中选择一个列时间，PD将会返回这个Series对象表示那一列。
DataFrames use Series objects to represent columns. When we select a single column from a DataFrame, pandas will return the Series object representing that column. By default, pandas indexes each individual Series object in a DataFrame with the integer data type. Each value in the Series has a unique integer index, or position. Like most Python data structures, the Series object uses 0-indexing. The indexing ranges from 0 to n-1, where n is the number of rows. We can use an integer index to select an individual value in a Series if we know its position.

Numpy和Series都可以通过方括号进行切片和选择值。
With both NumPy arrays and Series objects, we can pass integer indexes into bracket notation to slice and select values. With Series objects, however, we can also specify custom indexes.

To explore this idea further, let's use two Series objects representing the film names and Rotten Tomatoes scores.
'''
fandango = pd.read_csv('fandango_score_comparison.csv')
series_film = fandango['FILM']
series_rt = fandango['RottenTomatoes']

print(series_film)
print(series_rt)


## 3. Custom Indexes ##

'''
## 这节讲 根据两列Series数据，定义一个新的SeriesA。一列作为A的data，第二列作为index，这个index是电影名字的string。

Q：已知电影名series，求同索引的下的series_rt，即电影名对应的分数

这里的Series都可以通过tolist()转换成list类型。
'''

# Import the Series object from pandas
from pandas import Series

film_names = series_film.values
rt_scores = series_rt.values

data = rt_scores.tolist()
index = film_names.tolist()
series_custom = Series(data, index)

series_custom[['Minions (2015)', 'Leviathan (2014)']]

print(series_custom)

## 4. Integer Index Preservation ##

'''
## 这节讲



Even though we specified that the Series object uses a custom string index, 
the object still has an internal integer index that we can use for selection. 
When it comes to indexes, Series objects act like both dictionaries and lists. 
We can access values with our custom index (like the keys in a dictionary), 
or the integer index (like the index in a list).
'''


series_custom = Series(rt_scores , index=film_names)
series_custom[['Minions (2015)', 'Leviathan (2014)']]

fiveten = series_custom[5:11]
print(fiveten)

## 5. Reindexing ##

'''
## 这节讲 Series中的reindex(), sorted()

## sorted(index)  给index排序，一般安装首字母数字、或字母顺序排序；
## reindex(index) 给这个Series按照新的index从新排序，相当于xls扩展其他行一起重新排序。
'''

original_index = series_custom.index

'''
第一次尝试，出错。被Learn的部分误导了。
sorted_by_index = original_index.tolist()
sorted_by_index = sorted_by_index.reindex()
'''
sorted_index  = sorted(original_index)
sorted_by_index = series_custom.reindex(sorted_index)



## 6. Sorting ##

'''
## 这节讲 sort_index() 和 sort_values()

## 1)sort_index(), Link:
http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.Series.sort_index.html
Series.sort_index(axis=0, level=None, ascending=True, inplace=False, sort_remaining=True)


## 2)sort_values(), Link:
http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.Series.sort_values.html
Series.sort_values(axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')
'''
import pandas as pd

sc1 = series_custom
print(sc1)

sc2 = pd.Series.sort_index(sc1)
sc3 = pd.Series.sort_values(sc1)
print(sc2[:10])
print(sc3[:10])
