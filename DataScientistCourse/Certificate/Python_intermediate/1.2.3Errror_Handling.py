## 2.Sets

'''
## 这节讲 【集合】的创建和相关方法
### 1）唯一化 list中的值
### 2）set，集合。
### 3）与list的区别，无序（无索引）；值唯一，不可重复
### 4）用set()创建【集合】。

### 方法1：set(listA)
### 举例：unique_animals = set(["Dog", "Cat", "Hippo", "Dog", "Cat", "Dog", "Dog", "Cat"])
print(unique_animals)
### output：
{'Hippo', 'Cat', 'Dog'}

### 可以用add(), remove(),list()，为set添加、移除值，以及转换成list类型。
'''
#print(legislators)

gender = []

for row in legislators:
    #split = row.split(',')
    gender.append(row[3])

'''
## 这里之前出现了一个小问题，就是针对list类型用了 split方法。split只用于string！
'''
    
gender = set(gender)
gender



## 3. Exploring the Dataset
'''
@author: murphywan
## 这节讲 拿到一个新的数据集，先探索些可能的patterns。要看values的唯一值，将list转化成set

### 比如：
### 1）缺失数据，N/A
### 2）明显有问题的数据，出生日期2050年
### 3）重复出现的数据，性别column，都是男
'''
party = []
for row in legislators:
    party.append(row[6])

party = set(party)

print(party)
print('-------------------------------')
print(legislators)

'''
我们发现，输出的结果中第一个就是空值，''
Output
{'', 'Popular Democrat', 'Democrat-Liberal', 'Nonpartisan', 'American', 'Democratic Republican', 
'Ind. Republican-Democrat', 'States Rights', 'Anti Jacksonian', 'Democrat', 'Conservative Republican', 
'Coalitionist', 'Anti-Jacksonian', 'Ind. Whig', 'Jackson Republican', 'Adams', 'Jacksonian', 'Silver Republican', 
'Anti Masonic', 'Socialist', 'Anti-Administration', 'Pro-Administration', 'Union', 'Conservative',
'Anti-Lecompton Democrat', 'Nullifier', 'Progressive', 'Federalist', 'Whig', 'Republican', 'Independent Democrat', 
'Unconditional Unionist', 'Democratic and Union Labor', 'Republican-Conservative', 'Constitutional Unionist',
'Free Silver', 'Free Soil', 'Independent', 'Farmer-Labor', 'Union Democrat', 'Anti Jackson', 'Unknown', 'Prohibitionist',
'Jackson', 'Liberal Republican', 'Readjuster', 'Unionist', 'Adams Democrat', 'Progressive Republican', 'Readjuster Democrat', 
'Ind. Democrat', 'Law and Order', 'Union Labor', 'Populist', 'National Greenbacker', 'Crawford Republican', 'Liberty', 
'American Labor', 'Ind. Republican', 'New Progressive'}
'''
