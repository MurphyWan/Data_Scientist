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
## 这节讲 汇总统计，按照三级，把每个级别的fare票价平均值汇总值算出来。
##
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

        


