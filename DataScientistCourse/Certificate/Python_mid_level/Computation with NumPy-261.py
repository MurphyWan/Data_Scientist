## 2. Array Comparisons ##

'''
# 说的是Numpy的强项，整个矩阵(1D or 2D)的比较，与一个标量比较。
# 把要比较的矩阵弄出来，然后通过 “==”与 一个string或者 数字比较

'''

import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', skip_header= 1, delimiter = ',', dtype= 'U75')
#print(world_alchohol)

countries_canada = world_alcohol[:,2]== "Canada"
years_1984 = world_alcohol[:,0]=='1984'

print(countries_canada)
print(years_1984)


## 3. Selecting Elements ##

'''
这节讲，通过比较可以选择1D ndarray的“元素”或者2D数组的“行”。（之前有看到过，不过还是比较有意思的。）
Comparisons give us the power to select elements in arrays using Boolean vectors


'''


import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', skip_header= 1, delimiter = ',', dtype= 'U75')

country_is_algeria = world_alcohol[:,2] == 'Algeria'
country_algeria = world_alcohol[country_is_algeria,:]


## 4. Comparisons with Multiple Conditions ##

'''
# 这节讲 “&”、 “|” 多条件的符号
'''

import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', skip_header= 1, delimiter = ',', dtype= 'U75')

is_algeria_and_1986 = (world_alcohol[:,0] == '1986') & (world_alcohol[:,2] == 'Algeria')
#print(world_alcohol[:,0] == '1986')
#print(world_alcohol[:,2] == 'Algeria')

rows_with_algeria_and_1986  = world_alcohol[is_algeria_and_1986,:]




## 5. Replacing Values ##

'''
# 这节讲 替换原有矩阵的某个值
用比较得出的boolean矩阵然后作为原矩阵的筛选条件，替换原有矩阵的的一列或者一行的数据
'''

import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', skip_header= 1, delimiter = ',', dtype= 'U75')

'''
first_column_1986 = world_alcohol[:,0] == '1986'
#world_alcohol[first_column_1986,0] = '2014' # 这个一定是放在row的位置吗？感觉这里选的是列，所以，应该放在"："的右侧；后面的0，一定是很上面的一致吗？
fourth_column_Wine = world_alcohol[:,3] == 'wine'
#world_alcohol[fourth_column_Wine,3] = 'Grog'
'''

'''
#第二次尝试，让在column中增加这个比较boolean，此时思路比较乱。最后，错！

first_column_1986 = world_alcohol[:,0] == '1986'
world_alcohol[:,0][first_column_1986] = '2014'

fourth_column_Wine = world_alcohol[:,3] == 'wine'
world_alcohol[:,3][fourth_column_Wine] = 'Grog'
'''

'''
第三次尝试，我承认，在这道题目上卡壳了20分钟，原因是在看过答案之后，并没有理解下面这样的用法：
world_alcohol[:,0][world_alcohol[:,0] == '1986'] = '2014'

如果说是对二维数组进行index，那么
1) world_alcohol[:,0]，表示第一列全体，是一维数组
2) world_alcohol[:,0] == '1986'，表示全体第一列中值等于1986的一个一维布尔数组
3) 那么问题来了，下面这个是啥？
world_alcohol[:,0][world_alcohol[:,0] == '1986']，表示行、列？
即:
[:,0]，表示行，所有行；  
[world_alcohol[:,0] == '1986']，表示列，是一个Boolean的index

查阅了《用Python进行数据分析》一书第93、94页的内容，但是也没有如下
这样的array[][]写法！！！

array[one string column][1D-array Boolean typ ]= 'string'的写法


'''

'''
first_column_1986 = world_alcohol[:,0] == '1986'
print(first_column_1986)

print(world_alcohol[:,0][world_alcohol[:,0]=='1986'])

'''


'''

# 为了能够过关，不纠结于此细节，我们就姑且按照能够过关的方式理解吧。
# array[][]，理解为array[行][列]，
此[行]，其实是包括所有行的第一列
此[列]，是一维Boolean 矩阵，这两个这么写，就是指在这包括所有行的第一列，凡是值为1986的，都被选中，然后通过赋值语句"="被替换成另一个字符串2014

'''
print(world_alcohol[:,0] == '1986')

world_alcohol[:,0][world_alcohol[:,0] == '1986'] = '2014'
world_alcohol[:,3][world_alcohol[:,3] == 'Wine'] = 'Grog'

## 6. Replacing Empty Strings ##

'''
# 这节讲 替换空字符串(把原来''的字符串替换成0)
# 导入的数据，在一开始就是unicode，所以所有的值都变成了string，如果要做值的计算，我们先得把列中的数据转换成float
# 步骤2
# 1）锁定指定列的空值部分，Boolean arrayA = data array[: , X] == ''
# 2）然后用data array[][]=0 , 更具体的写法：data array[: , X][ Boolean arrayA] = 0
'''
import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', skip_header= 1, delimiter = ',', dtype= 'U75')
#print(world_alcohol)

is_value_empty = world_alcohol[: , 4] == ''
world_alcohol[: , 4][ is_value_empty] = 0


## 7. Converting Data Types ##

'''
# 这节讲 转换ndarray的数据类型（因Numpy的array 元素数据类型必须完全一样，所以是一转全传）
# 主要用到astype()这个变量
'''
'''
# 第一次尝试，尽然没有通过。很奇怪，不知道为何会这样？（ ）
import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', skip_header= 1, delimiter = ',', dtype= 'U75')
alcohol_consumption = world_alcohol[:, 4]
alcohol_consumption = alcohol_consumption.astype(float)
print(alcohol_consumption)
'''
'''
# 第二次尝试，把前两行删掉，既然就ok了。
'''
alcohol_consumption = world_alcohol[:, 4]
alcohol_consumption = alcohol_consumption.astype(float)

#预计是上面的已经导入数据，而ship_header=1 跳掉了data的第一行。这样想也不对。
#因为报错的原因是ValueError: could not convert string to float: 

## 8. Computing with NumPy ##

'''
# 这节讲 几个计算方法，sum();mean(),axis
# axis (axis = 1, row; axis = 0 , column)
'''
print(alcohol_consumption)
# alcohol_consumption is a 1D ndarray
total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()


## 9. Total Annual Alcohol Consumption ##

'''
# 这节讲 简单统计
'''
'''
# 第1个问题：要一个Boolean matrix，即用多条件选择矩阵范围
canada_1986 = (world_alcohol[:,0]=='1986')& (world_alcohol[:,2]=='Canada')
#print(canada_1986)
output:
[False False False ..., False False False] #其结果是，过滤所有这两列中，不是这俩值的行！！！


# 讲指定列的空字符串替换成0
empty_data = canada_1986[:,4] == ''
canada_1986[:,4][empty_data] = 0
canada_alcohol = (canada_1986[:,4][empty_data] = 0).dtype(float)

total_canadian_dringking = canada_alcohol.sum()
'''
'''
#-------------------------以上第一次，尝试出错--------------------------
原因在于：canada_1986 = (world_alcohol[:,0]=='1986')& (world_alcohol[:,2]=='Canada')
这句话，我错把canada_1986当作一个数值array了，其实他是个以Boolean matirx。它是is_canada_1986，而不是canada_1986
正确的做法是：

再加一句 canada_1986 = world_alcohol[is_canada_1986,:]

is_canada_1986 = (world_alcohol[:,0]=='1986')& (world_alcohol[:,2]=='Canada')
print(is_canada_1986)       #1)
print(len(is_canada_1986))  #2)
print(world_alcohol.shape)  #3)

output:
#1) [False False False ..., False False False] #其结果是，过滤所有这两列中，不是这俩值的行！！！
#2) 3257
#3) (3257, 5)

这个结果，看懂了吧！！！为什么这样一句话 canada_1986 = world_alcohol[is_canada_1986,:] 可以选出canada_1986的array了。这是因为，这个1D-Boolean array的长度和 world_alcohol的行数一样，然后把这个1D-Boolean arrya 放到row的位置进行筛选，所以能从world——alcohol当中筛选出要的符合连个条件的2D array 行。

'''
'''
#理清思路，然后下面重新开些

is_canada_1986 = (world_alcohol[:,0]=='1986')& (world_alcohol[:,2]=='Canada')
canada_1986 = world_alcohol[is_canada_1986,:]
canada_alcohol = (canada_1986[:,4][canada_1986[:,4] == ''] = '0').astype(float) 
total_canadian_drinking = canada_alcohol.sum()

#-------------------------以上第二次，尝试出错--------------------------
# 报错。看完答案，为什么这里的第一个canada_1986[:,4]是canada_alcohol? 
# 我们还是老老实实一步一步来吧，还不会走之前，我已经想飞了，这个确实不太稳健。
'''
is_canada_1986 = (world_alcohol[:,0]=='1986')& (world_alcohol[:,2]=='Canada')
canada_1986 = world_alcohol[is_canada_1986,:]
#print(canada_1986[:,4])
#the output is : ['0' '3.11' '4.87' '1.33']

canada_alcohol = canada_1986[:,4]
empty = canada_alcohol == ''
#canada_alcohol = canada_alcohol[empty] ='0' #这里用‘0’而不是0，是因为这列的其他值是string，numpy array元素类型必须一致。然后，再用astype()一起调整。你看一步一步来，很自然地，这里就用到了canada_alcohol，而不是canada_1986。说明稳步走，很重要，不易出错！！！
'''
#------以上这句报错了。 
#TypeError: only integer scalar arrays can be converted to a scalar index
# 看答案，没有前面的赋值语句！
# 不是，canada_alcohol = canada_alcohol[empty] ='0'
# 而是，canada_alcohol[empty] ='0'
'''
canada_alcohol[empty] = '0'
canada_alcohol = canada_alcohol.astype(float)
total_canadian_drinking = canada_alcohol.sum()



#------以下是用当前最简方式重写
'''
is_canada_1986 = (world_alcohol[:,0]=='1986')& (world_alcohol[:,2]=='Canada')
canada_1986 = world_alcohol[is_canada_1986,:]
canada_alcohol = ((canada_alcohol([canada_1986[:,4] == ''])) = '0').astype(float) 
total_canadian_drinking = canada_alcohol.sum()

# 尝试以失败告终。以下是报错！

Output
  File "<ipython-input-1-2f0746af303c>", line 76
    canada_alcohol = ((canada_alcohol([canada_1986[:,4] == ''])) = '0').astype(float)
                                                                 ^
SyntaxError: invalid syntax

放一放，往前走！！！
'''



## 10. Calculating Consumption for Each Country ##

'''
# 这节讲 延续上一节，做简单统计。每个国家1989年的酒饮料消费量。
# 按照country、year的酒饮料消费情况（升），用字典来做。

# Output：----------------------------------------------
{'Afghanistan': 0.0,
 'Albania': 1.73,
 ...
 'Zimbabwe': 4.9199999999999999}
'''
'''
#-------------------------------------------------------
is_canada_1986 = (world_alcohol[:,0]=='1986')& (world_alcohol[:,2]=='Canada')
canada_1986 = world_alcohol[is_canada_1986,:]
canada_alcohol = canada_1986[:,4]
empty = canada_alcohol == ''
canada_alcohol[empty] = '0'
canada_alcohol = canada_alcohol.astype(float)
total_canadian_drinking = canada_alcohol.sum()

# -------------以上为上一节内容，这里做个参考-------------
'''

totals = {}
'''
#先把Learn的部分写出来：
'''

#获得给定年份的行
year = '1989' #给定年份
#is_year = world_alcohol[:,0] == year
#year = world_alcohol[:,0][is_year]

#Loop country
#countries = world_alcohol[:,2]

for each_c in countries:
    is_country_year = (world_alcohol[:,2] == each_c) & (world_alcohol[:,0] == year)
    country_year = world_alcohol[is_country_year,:]
    country_alcohol = country_year[:,4]
    empty = country_alcohol == ''
    country_alcohol[empty]= '0'
    country_alcohol = country_alcohol.astype(float)
    country_consumption = country_alcohol.sum()
    if each_c in totals:
        totals[each_c] = totals[each_c] + country_consumption
    else:
        totals[each_c] = country_consumption

      
totals
#------------------以上跑的结果没错，和答案比较了下，但就是过不了关，操！------------------
