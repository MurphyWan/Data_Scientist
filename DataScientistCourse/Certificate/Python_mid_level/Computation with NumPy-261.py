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