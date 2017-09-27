## 2. Array Comparisons ##

'''
# ˵����Numpy��ǿ���������(1D or 2D)�ıȽϣ���һ�������Ƚϡ�
# ��Ҫ�Ƚϵľ���Ū������Ȼ��ͨ�� ��==���� һ��string���� ���ֱȽ�

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
��ڽ���ͨ���ȽϿ���ѡ��1D ndarray�ġ�Ԫ�ء�����2D����ġ��С�����֮ǰ�п��������������ǱȽ�����˼�ġ���
Comparisons give us the power to select elements in arrays using Boolean vectors


'''


import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', skip_header= 1, delimiter = ',', dtype= 'U75')

country_is_algeria = world_alcohol[:,2] == 'Algeria'
country_algeria = world_alcohol[country_is_algeria,:]


## 4. Comparisons with Multiple Conditions ##

'''
# ��ڽ� ��&���� ��|�� �������ķ���
'''

import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', skip_header= 1, delimiter = ',', dtype= 'U75')

is_algeria_and_1986 = (world_alcohol[:,0] == '1986') & (world_alcohol[:,2] == 'Algeria')
#print(world_alcohol[:,0] == '1986')
#print(world_alcohol[:,2] == 'Algeria')

rows_with_algeria_and_1986  = world_alcohol[is_algeria_and_1986,:]




## 5. Replacing Values ##

'''
# ��ڽ� �滻ԭ�о����ĳ��ֵ
�ñȽϵó���boolean����Ȼ����Ϊԭ�����ɸѡ�������滻ԭ�о���ĵ�һ�л���һ�е�����
'''

import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', skip_header= 1, delimiter = ',', dtype= 'U75')

'''
first_column_1986 = world_alcohol[:,0] == '1986'
#world_alcohol[first_column_1986,0] = '2014' # ���һ���Ƿ���row��λ���𣿸о�����ѡ�����У����ԣ�Ӧ�÷���"��"���Ҳࣻ�����0��һ���Ǻ������һ����
fourth_column_Wine = world_alcohol[:,3] == 'wine'
#world_alcohol[fourth_column_Wine,3] = 'Grog'
'''

'''
#�ڶ��γ��ԣ�����column����������Ƚ�boolean����ʱ˼·�Ƚ��ҡ���󣬴�

first_column_1986 = world_alcohol[:,0] == '1986'
world_alcohol[:,0][first_column_1986] = '2014'

fourth_column_Wine = world_alcohol[:,3] == 'wine'
world_alcohol[:,3][fourth_column_Wine] = 'Grog'
'''

'''
�����γ��ԣ��ҳ��ϣ��������Ŀ�Ͽ�����20���ӣ�ԭ�����ڿ�����֮�󣬲�û����������������÷���
world_alcohol[:,0][world_alcohol[:,0] == '1986'] = '2014'

���˵�ǶԶ�ά�������index����ô
1) world_alcohol[:,0]����ʾ��һ��ȫ�壬��һά����
2) world_alcohol[:,0] == '1986'����ʾȫ���һ����ֵ����1986��һ��һά��������
3) ��ô�������ˣ����������ɶ��
world_alcohol[:,0][world_alcohol[:,0] == '1986']����ʾ�С��У�
��:
[:,0]����ʾ�У������У�  
[world_alcohol[:,0] == '1986']����ʾ�У���һ��Boolean��index

�����ˡ���Python�������ݷ�����һ���93��94ҳ�����ݣ�����Ҳû������
������array[][]д��������

array[one string column][1D-array Boolean typ ]= 'string'��д��


'''

'''
first_column_1986 = world_alcohol[:,0] == '1986'
print(first_column_1986)

print(world_alcohol[:,0][world_alcohol[:,0]=='1986'])

'''


'''

# Ϊ���ܹ����أ��������ڴ�ϸ�ڣ����Ǿ͹��Ұ����ܹ����صķ�ʽ���ɡ�
# array[][]�����Ϊarray[��][��]��
��[��]����ʵ�ǰ��������еĵ�һ��
��[��]����һάBoolean ������������ôд������ָ������������еĵ�һ�У�����ֵΪ1986�ģ�����ѡ�У�Ȼ��ͨ����ֵ���"="���滻����һ���ַ���2014

'''
print(world_alcohol[:,0] == '1986')

world_alcohol[:,0][world_alcohol[:,0] == '1986'] = '2014'
world_alcohol[:,3][world_alcohol[:,3] == 'Wine'] = 'Grog'

## 6. Replacing Empty Strings ##

'''
# ��ڽ� �滻���ַ���(��ԭ��''���ַ����滻��0)
# ��������ݣ���һ��ʼ����unicode���������е�ֵ�������string�����Ҫ��ֵ�ļ��㣬�����ȵð����е�����ת����float
# ����2
# 1������ָ���еĿ�ֵ���֣�Boolean arrayA = data array[: , X] == ''
# 2��Ȼ����data array[][]=0 , �������д����data array[: , X][ Boolean arrayA] = 0
'''
import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', skip_header= 1, delimiter = ',', dtype= 'U75')
#print(world_alcohol)

is_value_empty = world_alcohol[: , 4] == ''
world_alcohol[: , 4][ is_value_empty] = 0


## 7. Converting Data Types ##

'''
# ��ڽ� ת��ndarray���������ͣ���Numpy��array Ԫ���������ͱ�����ȫһ����������һתȫ����
# ��Ҫ�õ�astype()�������
'''
'''
# ��һ�γ��ԣ���Ȼû��ͨ��������֣���֪��Ϊ�λ��������� ��
import numpy as np

world_alcohol = np.genfromtxt('world_alcohol.csv', skip_header= 1, delimiter = ',', dtype= 'U75')
alcohol_consumption = world_alcohol[:, 4]
alcohol_consumption = alcohol_consumption.astype(float)
print(alcohol_consumption)
'''
'''
# �ڶ��γ��ԣ���ǰ����ɾ������Ȼ��ok�ˡ�
'''
alcohol_consumption = world_alcohol[:, 4]
alcohol_consumption = alcohol_consumption.astype(float)

#Ԥ����������Ѿ��������ݣ���ship_header=1 ������data�ĵ�һ�С�������Ҳ���ԡ�
#��Ϊ�����ԭ����ValueError: could not convert string to float: 

## 8. Computing with NumPy ##

'''
# ��ڽ� �������㷽����sum();mean(),axis
# axis (axis = 1, row; axis = 0 , column)
'''
print(alcohol_consumption)
# alcohol_consumption is a 1D ndarray
total_alcohol = alcohol_consumption.sum()
average_alcohol = alcohol_consumption.mean()


## 9. Total Annual Alcohol Consumption ##

'''
# ��ڽ� ��ͳ��
'''
'''
# ��1�����⣺Ҫһ��Boolean matrix�����ö�����ѡ�����Χ
canada_1986 = (world_alcohol[:,0]=='1986')& (world_alcohol[:,2]=='Canada')
#print(canada_1986)
output:
[False False False ..., False False False] #�����ǣ����������������У���������ֵ���У�����


# ��ָ���еĿ��ַ����滻��0
empty_data = canada_1986[:,4] == ''
canada_1986[:,4][empty_data] = 0
canada_alcohol = (canada_1986[:,4][empty_data] = 0).dtype(float)

total_canadian_dringking = canada_alcohol.sum()
'''
'''
#-------------------------���ϵ�һ�Σ����Գ���--------------------------
ԭ�����ڣ�canada_1986 = (world_alcohol[:,0]=='1986')& (world_alcohol[:,2]=='Canada')
��仰���Ҵ��canada_1986����һ����ֵarray�ˣ���ʵ���Ǹ���Boolean matirx������is_canada_1986��������canada_1986
��ȷ�������ǣ�

�ټ�һ�� canada_1986 = world_alcohol[is_canada_1986,:]

is_canada_1986 = (world_alcohol[:,0]=='1986')& (world_alcohol[:,2]=='Canada')
print(is_canada_1986)       #1)
print(len(is_canada_1986))  #2)
print(world_alcohol.shape)  #3)

output:
#1) [False False False ..., False False False] #�����ǣ����������������У���������ֵ���У�����
#2) 3257
#3) (3257, 5)

�������������˰ɣ�����Ϊʲô����һ�仰 canada_1986 = world_alcohol[is_canada_1986,:] ����ѡ��canada_1986��array�ˡ�������Ϊ�����1D-Boolean array�ĳ��Ⱥ� world_alcohol������һ����Ȼ������1D-Boolean arrya �ŵ�row��λ�ý���ɸѡ�������ܴ�world����alcohol����ɸѡ��Ҫ�ķ�������������2D array �С�

'''
'''
#����˼·��Ȼ���������¿�Щ

is_canada_1986 = (world_alcohol[:,0]=='1986')& (world_alcohol[:,2]=='Canada')
canada_1986 = world_alcohol[is_canada_1986,:]
canada_alcohol = (canada_1986[:,4][canada_1986[:,4] == ''] = '0').astype(float) 
total_canadian_drinking = canada_alcohol.sum()

#-------------------------���ϵڶ��Σ����Գ���--------------------------
# ��������𰸣�Ϊʲô����ĵ�һ��canada_1986[:,4]��canada_alcohol? 
# ���ǻ�������ʵʵһ��һ�����ɣ���������֮ǰ�����Ѿ�����ˣ����ȷʵ��̫�Ƚ���
'''
is_canada_1986 = (world_alcohol[:,0]=='1986')& (world_alcohol[:,2]=='Canada')
canada_1986 = world_alcohol[is_canada_1986,:]
#print(canada_1986[:,4])
#the output is : ['0' '3.11' '4.87' '1.33']

canada_alcohol = canada_1986[:,4]
empty = canada_alcohol == ''
#canada_alcohol = canada_alcohol[empty] ='0' #�����á�0��������0������Ϊ���е�����ֵ��string��numpy arrayԪ�����ͱ���һ�¡�Ȼ������astype()һ��������㿴һ��һ����������Ȼ�أ�������õ���canada_alcohol��������canada_1986��˵���Ȳ��ߣ�����Ҫ�����׳�������
'''
#------������䱨���ˡ� 
#TypeError: only integer scalar arrays can be converted to a scalar index
# ���𰸣�û��ǰ��ĸ�ֵ��䣡
# ���ǣ�canada_alcohol = canada_alcohol[empty] ='0'
# ���ǣ�canada_alcohol[empty] ='0'
'''
canada_alcohol[empty] = '0'
canada_alcohol = canada_alcohol.astype(float)
total_canadian_drinking = canada_alcohol.sum()



#------�������õ�ǰ���ʽ��д
'''
is_canada_1986 = (world_alcohol[:,0]=='1986')& (world_alcohol[:,2]=='Canada')
canada_1986 = world_alcohol[is_canada_1986,:]
canada_alcohol = ((canada_alcohol([canada_1986[:,4] == ''])) = '0').astype(float) 
total_canadian_drinking = canada_alcohol.sum()

# ������ʧ�ܸ��ա������Ǳ���

Output
  File "<ipython-input-1-2f0746af303c>", line 76
    canada_alcohol = ((canada_alcohol([canada_1986[:,4] == ''])) = '0').astype(float)
                                                                 ^
SyntaxError: invalid syntax

��һ�ţ���ǰ�ߣ�����
'''



## 10. Calculating Consumption for Each Country ##

'''
# ��ڽ� ������һ�ڣ�����ͳ�ơ�ÿ��������1989��ľ�������������
# ����country��year�ľ�����������������������ֵ�������

# Output��----------------------------------------------
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

# -------------����Ϊ��һ�����ݣ����������ο�-------------
'''

totals = {}
'''
#�Ȱ�Learn�Ĳ���д������
'''

#��ø�����ݵ���
year = '1989' #�������
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

      

#------------------�����ܵĽ��û���ʹ𰸱Ƚ����£������ǹ����˹أ��٣�------------------
#�ҵ�ԭ���ˣ������ҵ����⡣countriesϵͳ�Ѿ�������ˡ����ֶ�����һ��countries = world_alcohol[:,2]���е���һ���ˡ�

totals

## 11. Finding the Country that Drinks the Most ##

'''
# ��ڽ� �ҵ����ܺȵĹ��ҡ�
# ����x��������max����ϡ�����ϵͳ�Ѿ������ֵ�total��������������Ϊkey/������Ϊvalue�ļ�ֵ�ԡ�
#��print(totals)�Ϳ��Կ�����
'''

highest_value = 0
highest_key = None

# hkey means a country as the key in the totals dict.
# ����hkey���ֵ��forѭ����Ϊʲô��ָ���ң�Ӧ����python�����ֵ��key��Ϊfor�Ĺؼ������ɣ�
for hkey in totals:
    if totals[hkey] > highest_value:
        highest_value = totals[hkey]
        highest_key = hkey
        #print(highest_value, highest_key)

highest_key



## 12.Next Step
'''
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
