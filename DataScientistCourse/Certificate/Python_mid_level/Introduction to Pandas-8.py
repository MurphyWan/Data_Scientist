'''
### 1
您现在应该对NumPy有一个很好的基础，并处理您的数据问题。NumPy比二维list容易得多，因为：

1、对数据执行计算很容易。
2、数据索引和切片更快更容易。
3、我们可以快速转换数据类型。

总之，NumPy使Python中的数据更加高效。广泛应用于这个原因，特别是机器学习。

您可能已经注意到NumPy在过去两个任务中遇到了一些限制。例如：

1、数组中的所有项都必须具有相同的数据类型。对于许多数据集，这使得数组在使用时会麻烦。
2、列和行必须通过数字引用，当您在列名和列的数字来回往复时，会引起混淆。

在接下来的几个任务中，我们将了解Pandas库，这是最流行的数据分析库之一。Pandas建立在NumPy上，但是更好地解决了NumPy的局限性。
'''


## 3. Read in a CSV file ##

'''
### 这节讲
'''
import pandas as pd

food_info = pd.read_csv('food_info.csv')
print(food_info, type(food_info))

## 4. Exploring the DataFrame ##

'''
### 这节讲 Pandas中最基础的方法和属性
例如：
pd.head()
pd.columns
pd.shape
dimensions = pd.shape
rows = dimensions[0]
columns = dimensions[1]
'''

print(food_info.head(3))
dimensions = food_info.shape
print(dimensions)
num_rows = dimensions[0]
print(num_rows)
num_cols = dimensions[1]
print(num_cols)

first_twenty = food_info.head(20)

'''
### 5 Indexing
当您将文件读入DataFrame时，pandas会使用第一行中的值（也称为标题）作为列标签和以及行数作为行标签。标签统称为索引index。DataFrame包含行索引和列索引。


'''


'''
### 6 Series
该Series对象是Pandas用来表示行和列的核心数据结构。Series是与NumPy向量类似的值的标记集合。Series对象的主要优点是可以使用【非整数标签】。NumPy数组只能使用整数标签进行索引。

当从DataFrame返回行或列时，Pandas利用此功能提供更多上下文。例如，当您从DataFrame中选择一行时，而不是仅将该行中的值作为列表返回，pandas会返回包含列标签的Series对象以及相应的值：
'''


## 7. Selecting a row ##

'''
### 这节讲 loc[]方法
'''


hundredth_row = food_info.loc[99]
print(hundredth_row)

## 8. Data types ##

'''
###这节讲 DataFrame.dtypes
'''


print(food_info.dtypes)

## 9. Selecting multiple rows ##

'''
### 这节讲 选取多行，还是用.loc[]
 1) 方法一：pass in either a [slice] of row labels, or 
 2) 方法二：a [list] of row labels and pandas will return a dataframe
 
 DataFrame.loc[start row : end row]
 
'''

# Slicing
print("Rows 3, 4, 5 and 6")
print(food_info.loc[3:6])

# List
print("Rows 2, 5, and 10")
two_five_ten = [2,5,10]
print(food_info.loc[two_five_ten])

#-------------以上为原题内容------------------

last_rows = food_info.loc[len(food_info)-5:] # 显示最后5行


## 10. Selecting individual columns ##

'''
## 这节讲 获取一列 
'''

# Series object.
#ndb_col = food_info["NDB_No"]
#print(ndb_col)

# Display the type of the column to confirm it's a Series object.
#print(type(ndb_col))

#---------------the above is original code-------------------

saturated_fat = food_info['FA_Sat_(g)']
cholesterol = food_info['Cholestrl_(mg)']
#print(saturated_fat)
#print(cholesterol)
print(food_info)


## 11. Selecting multiple columns by name ##

'''
## 这节讲 选择多列，通过列名选
方法：DataFrame[['列名1', '列名2']]，注意：这里是这样的用法[[,]]

'''
zinc_copper = food_info[["Zinc_(mg)", "Copper_(mg)"]]

columns = ["Zinc_(mg)", "Copper_(mg)"]
zinc_copper = food_info[columns]


#--------- the above is some old code--------------------

selenium_thiamin = food_info[['Selenium_(mcg)','Thiamin_(mg)']]

## 12. Practice ##

'''
## 这节讲

'''

#print(food_info.columns)
#print(food_info.head(2))
#--------- the above is some old code--------------------

gram_columns = food_info.columns.tolist()
#print(gram_columns) #打印显示：返回一个一维的list，其中元素都是string

'''
# 第一次尝试，出错。

gram_columns = food_info.columns.tolist()

suffix = "(g)"
for each in gram_columns:
    if each.endswith(suffix):
       gram_columns.append(each)

gram_df = food_info.columns[gram_columns]

print(gram_df.head(3)) 

【原因】应该是gram_columns 已经被明确定义，且有值。但是在以轮询它自己的for循环中又再次赋予它新的值，改写了它，所以，陷入死循环了。

gram_columns = yyy

for xxx in gram_columns:
   if xxx
      gram_columns.append(xxx)

改进方法是：它只能被用一次，要吗for轮询，要吗append()添加到其他list
'''

columns_list = food_info.columns.tolist()
gram_columns = []

suffix = "(g)"
for each in columns_list:
    if each.endswith(suffix):
       gram_columns.append(each)

gram_df = food_info[gram_columns] 
'''
# 这句写错了！food_info.columns[gram_columns] 应该是pd[['列名1'，‘列名2’]]，而gram_columns已经是一个list了，即有一层方括号[]，所以这里括号就一层，就ok了。
'''
print(gram_df.head(3)) 



