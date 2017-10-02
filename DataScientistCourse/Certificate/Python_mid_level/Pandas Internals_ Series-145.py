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
