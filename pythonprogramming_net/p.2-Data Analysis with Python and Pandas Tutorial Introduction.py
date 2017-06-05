# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 21:53:04 2017

@author: Administrator
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,53,34,45,64,34],
             'Bounced Rate':[65,72,62,64,54,66]}

df = pd.DataFrame(web_stats)
print(df)
print(df.head())
print(df.tail(2))

#plt.plot(df)
#plt.plot(df.head())
#plt.plot(df.tail(2))

#用set_index将Day设置为索引,(使用set_index会产生一个新的df)
print(df.set_index('Day'))
print(df.head())

df.set_index('Day', inplace = True)
print(df.head())

print(df['Visitors'])
print(df.Visitors)

#print(df.Bounced Rate)   #如果作为属性，因为该属性名中有空格，因此会报错
print(df['Bounced Rate'])

print(df[['Bounced Rate','Visitors']])  #从点可以看出来，DataFrame是一个多维数组

print(df.Visitors.tolist()) #把array转换成list

#print(df[['Bounced Rate','Visitors']].tolist()) #这样写会报错，因为这已经是二维数组了，tolist不行
#针对上面这一行，怎么处理呢？ 
#想到numpy了，导入numpy库先，然后用np.array封装
print(np.array(df[['Bounced Rate','Visitors']]))

#然后导入DF中
df2 = pd.DataFrame(np.array(df[['Bounced Rate', 'Visitors']]))
print(df2)

df3 = pd.DataFrame(np.array(df[['Bounced Rate' , 'Visitors']]),
                   index = ['one', 'two', 'three', 'four', 'five', 'six'],
                   columns = ['Bounced_Rate', 'Visitors'])

print(df3)
