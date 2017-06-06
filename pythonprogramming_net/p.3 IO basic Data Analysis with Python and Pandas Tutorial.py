# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 14:41:03 2017

@author: Administrator
"""

import pandas as pd

"""
df  = pd.read_csv('p3-ZILL-Z77006_.csv')

df.set_index('Date', inplace = True)
df.to_csv('newcsv2.csv')
"""

#index_col = 0,表示不用自带的索引列。
df = pd.read_csv('newcsv2.csv', index_col = 0) 
print(df.head())


#设置列名为 Austin——HPI
df.columns = ['Austin_HPI']
print(df.head())
#保存到csv文件里面
df.to_csv('newcsv3.csv')

#保存一份csv，干掉表头header
df.to_csv('newcsv4.csv', header=False)

#导入没有header的数据时，增加表头header,且不雅index列
df = pd.read_csv('newcsv4.csv', names=['Date','Austin_HPI'], index_col=0)
print(df.head())

#输出保存为html,原本DataFrame中的数据将保存为html中的table里面
df.to_html('newhtml.html')


#变更 列名，用rename
df.rename(columns={'Austin_HPI':'77006_HPI}, inplace = True)