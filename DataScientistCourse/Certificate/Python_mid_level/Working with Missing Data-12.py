## 2. Introduction ##

'''
## 这节讲
'''

import pandas as pd

titanic_survival = pd.read_csv('titanic_survival.csv')
titanic_survival

## 3. Finding the Missing Data ##

'''
## 这节讲 pd.isnull()看那个值是空的

pd.isnull() 取自一个series ，用于一个series，返回Boolean类型的series
'''

age = titanic_survival["age"]
print(age.loc[10:20])
'''
#------------the above is the original code-------------
'''
age_is_null = age.isnull()
age_null_true = age[age_is_null] # 选择age列中是null的元素
age_null_count = len(age_null_true)

print(age_null_count)




## 4. Whats the big deal with missing data? ##

'''
## 这节讲 如果数值型列中包括有NA值，那么要做统计，必须先有过滤缺失数据

## pd.isnull() 取自一个series ，用于一个series，返回Boolean类型的series

##方法：直接用pd.dropna()，即可把column中含有NA的丢弃掉。 
##      mean = sum(剔除na的列A) / len(剔除na的列A)
'''
age_is_null = pd.isnull(titanic_survival["age"])

age = titanic_survival["age"]
age_not_null = age.dropna()
correct_mean_age = sum(age_not_null) / len(age_not_null)

'''
完成后，我看了答案的写法。很有意思的发现：
good_ages = titanic_survival["age"][age_is_null == False]

age_is_null == False ，这是负负得正的意思咩。age_is_null，其中False的是非空值；True的说明是Na值。所以要取False的值，那么就是age_is_null == False
下面跟着再敲一遍。
'''
good_age = age[age_is_null == False]
correct_mean_age = sum(good_age) / len(good_age)



## 5. Easier Ways to Do Math ##

'''
## 这节讲 Series.mean() ,不会把NA值计算在内。
'''

correct_mean_age = titanic_survival["age"].mean()

correct_mean_fare = titanic_survival['fare'].mean()

## 6. Calculating Summary Statistics ##

'''
## 这节讲 汇总统计，按照三级，把每个级别(Group)的fare票价平均值汇总值算出来。
## 方法：用字典，key就是group的分类，这里是1、2、3；拿到这个类的所有rows即indecis

## 在这里有点卡壳，原因在于，
1）没有想到是通过先把一列pclass做【比较】，
2）然后，【拿到】符合条件所有的rows，这个rows其实是带有indecis的series
3）接着，这样就可以rows['fare']拿到符合pclass = 1的所有fare
4）最后，就可以统计这一类全体的值（统计函数，一定是计算某一类的全体值的，NA值像mean（）等方法会自动过滤）

我自己最早设想的用嵌套for 循环是否可以解呢？（）
以后再说。
'''

passenger_classes = [1, 2, 3]
fares_by_class = {}

'''
## 运行很长时间，一直没有结果。估计死循环了。
for each_class in passenger_classes:
    if each_class == titanic_survival['pclass']:
        if each_class in fares_by_class:
            fares_by_class[each_class] = fares_by_class[each_class] + titanic_survival['fare']
        else:
            fares_by_class[each_class] = titanic_survival['fare']

fares_by_class
'''
for c in passenger_classes:
    '''
    #先把一列pclass做【比较】,赋值给新的DF，【拿到】符合条件所有的rows，这个rows其实是带有indecis的series
    '''
    pclass_rows = titanic_survival[titanic_survival['pclass'] == c] 
    #print(pclass_rows)
    '''
    #这样就可以rows['fare']拿到符合pclass = 1的所有fare
    '''
    pclass_fares = pclass_rows['fare'] 
    
    '''
    # 就可以统计这一类全体的值（统计函数，一定是计算某一类的全体值的，NA值像mean（）等方法会自动过滤）
    '''
    pclass_fares_mean = pclass_fares.mean() 
    '''
    # 给字典赋值，同时定义key
    '''
    fares_by_class[c] = pclass_fares_mean 


        




## 7. Making Pivot Tables ##

'''
## 这节讲 拿上一节的问题，用新方法数据透视表来解决，这里使用DataFrame.pivot_table()

## passenger_class_fares = titanic_survival.pivot_table(index="pclass", values="fare", aggfunc=numpy.mean)

## 参数说明
1) index：要对那一列做group？
2) values: 我们要对那一列进行计算？
3) aggfunc: 指定一种计算方式，如用numpy.mean，缺省情况下就是mean，所以可以omit
'''
passenger_survival = titanic_survival.pivot_table(index="pclass", values="survived")

ts = titanic_survival
passenger_age = ts.pivot_table(index = 'pclass', values = 'age')
print(passenger_age)

'''
#Output:

pclass
1.0    39.159918
2.0    29.506705
3.0    24.816367
Name: age, dtype: float64
'''



## 8. More Complex Pivot Tables ##

'''
## 这节讲 还是DF.pivot_table()； 传一堆列名的list给到values，一次可以对多列进行计算

'''

import numpy as np

df_ts = titanic_survival
all_col = df_ts.columns.tolist()
two_col = ['fare', 'survived']
#print(all_col)
port_stats = df_ts.pivot_table(index = 'embarked', values = two_col, aggfunc = numpy.sum)
print(port_stats)



## 9. Drop Missing Values ##

'''
## 这节讲 matirx(DF)中的缺失值处理；以及把DF.dropna()中的主要参数搞清楚。
之前讲到的都是在ventor(Series)中处理缺失值

## 方法：DF.dropna() P150
## 参数介绍：
1) axis = 0 or axis = 'index'
2) axis = 1 or axis = 'columns'
3) how = 'all' or how = 'any'
4) thresh 在axis= 0 ，即rows方向最多保留thresh个NaN值。有待确认 ( ) 
5) subset =[''[,'']] ，‘’中为要丢弃NaN值的列名

详情参阅API:
DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
'''
df_ts = titanic_survival

drop_na_rows = titanic_survival.dropna(axis=0)

drop_na_columns = df_ts.dropna(axis=1)
new_titanic_survival = df_ts.dropna(axis=0, subset=['age','sex'])


## 10. Using iloc to Access Rows by Position ##

'''
## 这节讲 选择值为整数的行，用DF.iloc[slicing]

iloc[] 缺省选择行，
loc[] 选择行 ,row的index label为整数时用
ix 
以上这几者的区别，详见：https://stackoverflow.com/questions/31593201/pandas-iloc-vs-ix-vs-loc-explanation
'''

# We have already sorted new_titanic_survival by age
first_five_rows = new_titanic_survival.iloc[0:5]

print(new_titanic_survival.columns)
new_ts = new_titanic_survival

first_ten_rows = new_ts.iloc[0:10]
row_position_fifth = new_ts.iloc[4]
row_index_25 = new_ts.loc[25]




## 11. Using Column Indexes ##

'''
## 这节讲 loc[] and iloc[]
We can also index columns using both the loc[] and iloc[] methods

1) loc[]和iloc[]都可以选择行和列;
2) iloc一定要列是整型值的；
3) loc可以是字符串、和整型;
4) 如果用iloc的话，最左边的column为0。
'''

first_row_first_column = new_titanic_survival.iloc[0,0]
all_rows_first_three_columns = new_titanic_survival.iloc[:,0:3]
row_index_83_age = new_titanic_survival.loc[83,"age"]
row_index_766_pclass = new_titanic_survival.loc[766,"pclass"]

new_ts = new_titanic_survival
row_index_1100_age = new_ts.loc[1100, 'age']
row_index_25_survived = new_ts.loc[25,'survived']
five_rows_three_cols = new_ts.iloc[:5, :3]


## 12. Reindexing Rows ##

'''
## 这节讲 如果matrix的某一列进行排序，则indexes的顺序被打乱，不在是序列。

## 方法：DF.reset_index(),从0开始
## 1) 缺省情况下，这个方法通过增加额外一列，保留原来的index。
## 2) 当然也可以删除这个原来的index，使用参数
'''

new_ts = new_titanic_survival

titanic_reindexed = new_ts.reset_index(drop=True)
print(titanic_reindexed.iloc[:5,:3])


## 13. Apply Functions Over a DataFrame ##

'''
## 这节讲 执行复杂的计算 DF.apply()

## 功能描述：这个方法会不断轮询DF中的每个column，执行每一个【方法】
## 这题，编写一个function，带有一个参数，通过apply()将其做为series传递给每个columns

## 方法：DF.apply()要和一个涉及到以column为参数的函数一起使用。
'''
'''
--------------the below is the original code------------

def hundredth_row(column):
    hundredth_item = column.iloc[99]
    return hundredth_item

hundredth_row_var = titanic_survival.apply(hundredth_row)
'''
'''
题目：求DF中每一列null值的数量
'''
def null_col(column):
    count_null = len(column[column.isnull()])
    return count_null

column_null_count = titanic_survival.apply(null_col)



## 14. Applying a Function to a Row ##

'''
## 这节讲 还是DF.apply()，只是多了个参数axis=1,遍历rows，而不是columns

## 注意：这里axis= 1 才是遍历所有的【行】！！！
'''
def is_minor(row):
    if row["age"] < 18:
        return True
    else:
        return False

minors = titanic_survival.apply(is_minor, axis=1)

'''
------------the above is the original code------------
------------the below is the code written by myself---
'''
def is_adult(row):
    age = row['age']
    if pd.isnull(age):
        return 'unknown'
    elif age < 18:
        return 'minor'
    elif age >= 18:
        return 'adult'
    
age_labels = titanic_survival.apply(is_adult, axis=1)

## 15. Calculating Survival Percentage by Age Group ##

'''
## 这节讲
'''

print(titanic_survival['age_labels'])
'''
Output:

0         adult
1         minor
...
1308      adult
1309    unknown
Name: age_labels, dtype: object
'''
age_group_survival = titanic_survival.pivot_table(index= 'age_labels', values= 'survived', aggfunc= numpy.mean) 
