## 1. Shared Indexes ##

'''
# @author:murphywan
## 这节讲 pd.read_csv(), pd.head(), pd.index
'''
import pandas as pd

fandango = pd.read_csv('fandango_score_comparison.csv')
fandango.head(2)

fandango.index



## 2. Using Integer Indexes to Select Rows ##

'''
# @author:murphywan
## 这节讲 用pd.shape和iloc()，选择第一行和最后一行，创建一个新的pd！！！
'''
fandango = pd.read_csv('fandango_score_comparison.csv')

'''
第一次卡壳了，因为不知道怎么同时把第一行和最后一行写进一个pd中？
first = fandango.iloc[0]
last = fandango.iloc[len(fandango)-1]
参考了答案。 用pd.iloc[[row1,rowN]]
'''
'''
第二次错了，因为对pd.iloc[]已经忘记了，里面直接放整数型的index，或者 slicing，所以下面这个写法就错了。
first_ = fandango.iloc[0]
last_ = fandango.iloc[len(fandango)-1]
first_last = fandango.iloc[[first_, last_]]
'''
first_last = fandango.iloc[[0, len(fandango)-1]]



## 3. Using Custom Indexes ##

'''
# @author:murphywan
## 这节讲 pd.set_index(, inplace, drop)

DataFrame.set_index(keys, drop=True, append=False, inplace=False, verify_integrity=False)
http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.DataFrame.set_index.html#pandas.DataFrame.set_index
'''
fandango = pd.read_csv('fandango_score_comparison.csv')

fandango_films = fandango.set_index(fandango['FILM'], drop= False)
'''
## drop = False，保留原column，不要删除。
'''
print(fandango_films.index)
print('_________________________________________________________')
print(fandango_films)



## 4. Using a Custom Index for Selection ##

'''
# @author:murphywan
## 这节讲 选择指定的索引行 
'''

fandango_films
'''
第1种写法 结果错了，也许是python3不支持
#best_movies_ever = fandango_films[ index = ['The Lazarus Effect (2015)','Gett: The Trial of Viviane Amsalem (2015)','Mr. Holmes (2015)']]
'''

'''
第2种写法 结果错了，也许是python3不支持
#best_movies_ever = fandango_films[['The Lazarus Effect (2015)','Gett: The Trial of Viviane Amsalem (2015)','Mr. Holmes (2015)']]
'''
'''
第3种写法
'''
best_movies_ever = fandango_films.loc[['The Lazarus Effect (2015)','Gett: The Trial of Viviane Amsalem (2015)','Mr. Holmes (2015)']]




## 5. Apply() Logic Over the Columns in a Dataframe ##
'''
# @author:murphywan
## 这节讲 pd.apply()方法
'''
'''
Recall that a dataframe object represents both rows and columns as Series objects. 
The apply() method in pandas allows us to specify Python logic that we want to evaluate over the Series objects in a dataframe. 
Here are some examples of what we can accomplish using the apply() method:

    .Calculate the standard deviations for each numeric column
    .Lowercase all film names in the FILM column
    
The apply() method requires us to pass in the vectorized operation we want to apply over each Series object. 
The method runs over the dataframe's columns by default, but we can use the axis parameter to change this (which we'll do later). 
If the vectorized operation usually returns a single value (such as the NumPy std() function), 
it will return a Series object containing the computed value for each column. 
If it usually returns a value for each element (such as multiplying or dividing by 2), 
it will transform all of the values and return them as a dataframe.

In the following code cell, we select only the float columns, 
and assign the dataframe containing them to float_df. 
Then, we pass in the NumPy function std() as a lambda function to the dataframe method apply() in order to calculate the standard deviation of each column. 
Under the hood, pandas uses vectorized operations to apply the NumPy function for each iteration of the apply() method. 
It then returns a final Series object containing the standard deviations for each column (i.e., the film ratings).
'''
import numpy as np

# returns the data types as a Series
types = fandango_films.dtypes
print(types)
'''
Output
FILM                           object
RottenTomatoes                  int64
RottenTomatoes_User             int64
Metacritic                      int64
Metacritic_User               float64
IMDB                          float64
Fandango_Stars                float64
Fandango_Ratingvalue          float64
RT_norm                       float64
RT_user_norm                  float64
Metacritic_norm               float64
Metacritic_user_nom           float64
IMDB_norm                     float64
RT_norm_round                 float64
RT_user_norm_round            float64
Metacritic_norm_round         float64
Metacritic_user_norm_round    float64
IMDB_norm_round               float64
Metacritic_user_vote_count      int64
IMDB_user_vote_count            int64
Fandango_votes                  int64
Fandango_Difference           float64
dtype: object
'''

print('--------------------------------------')
# filter data types to just floats, index attributes returns just column names
float_columns = types[types.values == 'float64'].index
print(float_columns)
'''
Index(['Metacritic_User', 'IMDB', 'Fandango_Stars', 'Fandango_Ratingvalue',
       'RT_norm', 'RT_user_norm', 'Metacritic_norm', 'Metacritic_user_nom',
       'IMDB_norm', 'RT_norm_round', 'RT_user_norm_round',
       'Metacritic_norm_round', 'Metacritic_user_norm_round',
       'IMDB_norm_round', 'Fandango_Difference'],
      dtype='object')
'''
print('--------------------------------------')


# use bracket notation to filter columns to just float columns
float_df = fandango_films[float_columns]
print(float_df)

'''
                                                Metacritic_User  IMDB  \
FILM                                                                    
Avengers: Age of Ultron (2015)                              7.1   7.8   
Cinderella (2015)                                           7.5   7.1   
Ant-Man (2015)                                              8.1   7.8   
...

[146 rows x 15 columns]
'''
print('--------------------------------------')



# `x` is a Series object representing a column
deviations = float_df.apply(lambda x: np.std(x))

print(deviations)

## 6. Apply() Logic Over Columns: Practice ##

'''
# @author:murphywan
## 这节讲 Numpy.std(), pd.apply(), lambda。 我们可以使得每一columns的值都改变，然后返回一个新的DataFrame

'''
double_df = float_df.apply(lambda x: x*2)
print(double_df.head(1))

halved_df = float_df.apply(lambda x: x/2)
print(halved_df.head(1))

## 7. Apply() Over Dataframe Rows ##

'''
# @author:murphywan
## 这节讲 继续将apply() 只是作用于row，而不再是colunms, 所以要设置 axis = 1
'''
rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
rt_mt_deviations = rt_mt_user.apply(lambda x: np.std(x), axis=1)
print(rt_mt_deviations[0:5])


rm_user_norm = float_df[['RT_user_norm','Metacritic_user_nom']]
rt_mt_means = rm_user_norm.apply(lambda x:np.mean(x), axis=1)

rt_mt_means.head(5)
