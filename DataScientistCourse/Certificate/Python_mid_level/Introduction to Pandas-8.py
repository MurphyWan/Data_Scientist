'''
### 1
������Ӧ�ö�NumPy��һ���ܺõĻ����������������������⡣NumPy�ȶ�άlist���׵ö࣬��Ϊ��

1��������ִ�м�������ס�
2��������������Ƭ��������ס�
3�����ǿ��Կ���ת���������͡�

��֮��NumPyʹPython�е����ݸ��Ӹ�Ч���㷺Ӧ�������ԭ���ر��ǻ���ѧϰ��

�������Ѿ�ע�⵽NumPy�ڹ�ȥ����������������һЩ���ơ����磺

1�������е���������������ͬ���������͡�����������ݼ�����ʹ��������ʹ��ʱ���鷳��
2���к��б���ͨ���������ã��������������е�������������ʱ�������������

�ڽ������ļ��������У����ǽ��˽�Pandas�⣬���������е����ݷ�����֮һ��Pandas������NumPy�ϣ����Ǹ��õؽ����NumPy�ľ����ԡ�
'''


## 3. Read in a CSV file ##

'''
### ��ڽ�
'''
import pandas as pd

food_info = pd.read_csv('food_info.csv')
print(food_info, type(food_info))

## 4. Exploring the DataFrame ##

'''
### ��ڽ� Pandas��������ķ���������
���磺
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
�������ļ�����DataFrameʱ��pandas��ʹ�õ�һ���е�ֵ��Ҳ��Ϊ���⣩��Ϊ�б�ǩ���Լ�������Ϊ�б�ǩ����ǩͳ��Ϊ����index��DataFrame��������������������


'''


'''
### 6 Series
��Series������Pandas������ʾ�к��еĺ������ݽṹ��Series����NumPy�������Ƶ�ֵ�ı�Ǽ��ϡ�Series�������Ҫ�ŵ��ǿ���ʹ�á���������ǩ����NumPy����ֻ��ʹ��������ǩ����������

����DataFrame�����л���ʱ��Pandas���ô˹����ṩ���������ġ����磬������DataFrame��ѡ��һ��ʱ�������ǽ��������е�ֵ��Ϊ�б��أ�pandas�᷵�ذ����б�ǩ��Series�����Լ���Ӧ��ֵ��
'''


## 7. Selecting a row ##

'''
### ��ڽ� loc[]����
'''


hundredth_row = food_info.loc[99]
print(hundredth_row)

## 8. Data types ##

'''
###��ڽ� DataFrame.dtypes
'''


print(food_info.dtypes)

## 9. Selecting multiple rows ##

'''
### ��ڽ� ѡȡ���У�������.loc[]
 1) ����һ��pass in either a [slice] of row labels, or 
 2) ��������a [list] of row labels and pandas will return a dataframe
 
 DataFrame.loc[start row : end row]
 
'''

# Slicing
print("Rows 3, 4, 5 and 6")
print(food_info.loc[3:6])

# List
print("Rows 2, 5, and 10")
two_five_ten = [2,5,10]
print(food_info.loc[two_five_ten])

#-------------����Ϊԭ������------------------

last_rows = food_info.loc[len(food_info)-5:] # ��ʾ���5��


## 10. Selecting individual columns ##

'''
## ��ڽ� ��ȡһ�� 
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
## ��ڽ� ѡ����У�ͨ������ѡ
������DataFrame[['����1', '����2']]��ע�⣺�������������÷�[[,]]

'''
zinc_copper = food_info[["Zinc_(mg)", "Copper_(mg)"]]

columns = ["Zinc_(mg)", "Copper_(mg)"]
zinc_copper = food_info[columns]


#--------- the above is some old code--------------------

selenium_thiamin = food_info[['Selenium_(mcg)','Thiamin_(mg)']]

## 12. Practice ##

'''
## ��ڽ�

'''

#print(food_info.columns)
#print(food_info.head(2))
#--------- the above is some old code--------------------

gram_columns = food_info.columns.tolist()
#print(gram_columns) #��ӡ��ʾ������һ��һά��list������Ԫ�ض���string

'''
# ��һ�γ��ԣ�����

gram_columns = food_info.columns.tolist()

suffix = "(g)"
for each in gram_columns:
    if each.endswith(suffix):
       gram_columns.append(each)

gram_df = food_info.columns[gram_columns]

print(gram_df.head(3)) 

��ԭ��Ӧ����gram_columns �Ѿ�����ȷ���壬����ֵ������������ѯ���Լ���forѭ�������ٴθ������µ�ֵ����д���������ԣ�������ѭ���ˡ�

gram_columns = yyy

for xxx in gram_columns:
   if xxx
      gram_columns.append(xxx)

�Ľ������ǣ���ֻ�ܱ���һ�Σ�Ҫ��for��ѯ��Ҫ��append()��ӵ�����list
'''

columns_list = food_info.columns.tolist()
gram_columns = []

suffix = "(g)"
for each in columns_list:
    if each.endswith(suffix):
       gram_columns.append(each)

gram_df = food_info[gram_columns] 
'''
# ���д���ˣ�food_info.columns[gram_columns] Ӧ����pd[['����1'��������2��]]����gram_columns�Ѿ���һ��list�ˣ�����һ�㷽����[]�������������ž�һ�㣬��ok�ˡ�
'''
print(gram_df.head(3)) 



