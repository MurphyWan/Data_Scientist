## 2. Creating arrays ##

import numpy as np


vector = np.array([10,20,30])
matrix = np.array([[5,10,15],[20,25,30],[35,40,45]])

## 3. Array shape ##

import numpy as np

vector = np.array([10, 20, 30])
matrix = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])

vector_shape = vector.shape
matrix_shape = matrix.shape

print(vector_shape,matrix_shape)

## 4. Using NumPy ##

import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv',delimiter = ',')
print(type(world_alcohol),world_alcohol)

## 5. Data types ##

import numpy as np

#print(world_alcohol)
world_alcohol_dtype = world_alcohol.dtype
print(world_alcohol_dtype)

## 7. Reading in the data correctly ##

'''
主要是将genfromtxt（）的一些参数，及其怎么用？

# genfromtxt(parameter1, parameter2,..., parameterN)
# 1)skip_header
# 2)dtype, data = np.genfromtxt(s, dtype="i8,f8,S5") or dtype = None
# 3)delimiter = ','
# 4)skip_header = 1, 跳过第一行，基本上就是要跳过表头
'''

import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', skip_header = 1, delimiter = ',',dtype = 'U75')
print(world_alcohol)


## 8. Indexing arrays ##

'''
# 这节主要讲数组的索引，一维和二维的
# list_of_lists[0][2]

'''

import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', skip_header = 1, delimiter = ',',dtype = 'U75')

uruguay_other_1986 = world_alcohol[1][4]
third_country = world_alcohol[2][2]


## 9. Slicing arrays ##

import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', skip_header = 1, delimiter = ',',dtype = 'U75')

countries = world_alcohol[:,2]
alcohol_consumption = world_alcohol[:,4]

## 10. Slicing one dimension ##

import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', skip_header = 1, delimiter = ',',dtype = 'U75')

first_two_columns = world_alcohol[:,:2]
first_ten_years = world_alcohol[:10,0]
first_ten_rows = world_alcohol[:10,:]

## 11. Slicing arrays ##

import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', skip_header = 1, delimiter = ',',dtype = 'U75')

first_twenty_regions = world_alcohol[:20,1:3]