## 1.Sets

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
