## 1. Overview ##

'''
##这节讲 Pandas实践
'''

import pandas as pd

food_info = pd.read_csv('food_info.csv')
#food_info

col_names = food_info.columns.tolist()
print(col_names)
print(food_info.head(3))



## 2. Transforming a Column ##

''' 
## 这节讲  物理单位量转化（毫克->克 除以1000），so easy
'''

div_1000 = food_info["Iron_(mg)"] / 1000
add_100 = food_info["Iron_(mg)"] + 100
sub_100 = food_info["Iron_(mg)"] - 100
mult_2 = food_info["Iron_(mg)"]*2

sodium_grams = food_info['Sodium_(mg)'] / 1000
sugar_milligrams = food_info['Sugar_Tot_(g)'] * 1000


## 3. Performing Math with Multiple Columns ##

''' 
## 这节讲 pandas的两个数值列可以做四则算术运算，两个列对应同row的值做运算。然后返回一个series
'''

water_energy = food_info["Water_(g)"] * food_info["Energ_Kcal"]
print(water_energy[0:5])

grams_of_protein_per_gram_of_water = food_info['Protein_(g)'] / food_info['Water_(g)']
milligrams_of_calcium_and_iron = food_info['Calcium_(mg)'] + food_info['Iron_(mg)']

## 4. Create a Nutritional Index ##

''' 
## 这节讲  继续讲两个数值列可以做四则算术运算，两个列对应同row的值做运算。然后返回一个series
'''

weighted_protein = food_info['Protein_(g)'] * 2
weighted_fat = food_info['Lipid_Tot_(g)'] *(-0.75)

initial_rating = weighted_protein + weighted_fat

## 5. Normalizing Columns in a Data Set ##

''' 
## 这节讲 Series中列的【归一化】

方法：用columns中所有值除以该列最大值series.max()，这样，列中所有的值都在0-1之间。所谓的归一化。
'''

print(food_info["Protein_(g)"][0:5])
max_protein = food_info["Protein_(g)"].max()

normalized_protein = food_info['Protein_(g)'] / food_info['Protein_(g)'].max()
normalized_fat = food_info['Lipid_Tot_(g)'] / food_info['Lipid_Tot_(g)'].max()

## 6. Creating a New Column ##

''' 
## 这节讲 新增一column
将一个新的series新增到DataFrame中作为一列

## 方法： 取自DataFrameX，用于DataFrameX
## 1) series = DataFrameX['ColumnA'] +-*/ number (四则运算用其一种)
## 2) DataFrameX['ColumnB'] = series
'''

food_info['Normalized_Protein'] = food_info['Protein_(g)'] / food_info['Protein_(g)'].max() 
food_info['Normalized_Fat'] = food_info['Lipid_Tot_(g)'] /  food_info['Lipid_Tot_(g)'].max()

## 7. Create a Normalized Nutritional Index ##

''' 
## 这节讲
'''

food_info["Normalized_Protein"] = food_info["Protein_(g)"] / food_info["Protein_(g)"].max()
food_info["Normalized_Fat"] = food_info["Lipid_Tot_(g)"] / food_info["Lipid_Tot_(g)"].max()

food_info['Norm_Nutr_Index'] = 2 * food_info["Normalized_Protein"] - 0.75 * food_info["Normalized_Fat"]

## 8. Sorting a DataFrame by a Column ##

''' 
Sorting a DataFrame by a Column
## 这节讲 DataFrame 对象的方法sort_values()

## 方法：把列名放进去就好，DataFrame.sort_values("ColumnA") #字符串列名记得带上引号
## 默认情况下：对Column的值进行升序排列，返回一个新的DataFrame

详情请参考API：
http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_values.html
DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')

'''

food_info["Normalized_Protein"] = food_info["Protein_(g)"] / food_info["Protein_(g)"].max()
food_info["Normalized_Fat"] = food_info["Lipid_Tot_(g)"] / food_info["Lipid_Tot_(g)"].max()
food_info["Norm_Nutr_Index"] = 2*food_info["Normalized_Protein"] + (-0.75*food_info["Normalized_Fat"])

food_info.sort_values('Norm_Nutr_Index', inplace = True, ascending= False)

food_info