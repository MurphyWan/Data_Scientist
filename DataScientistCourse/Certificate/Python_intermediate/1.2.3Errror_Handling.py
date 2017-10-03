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

#---------------------------------------------------------------------------------------------------------------------------

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
#---------------------------------------------------------------------------------------------------------------------------

## 4. Missing Values

'''
@author: murphywan
## 这节讲 针对missing values进行填空

## 方法：针对list of lists，用for + if
        for row in rows:
            if row[1] == "":
                row[1] = "NAN"

### 处理缺失值的四个策略（这里讲第2点）：
1)删除包含缺少数据的行。
2)用指定的值填充空字段。
3)用计算的值填充空字段。
4)与确实数据可以一起使用的分析技术。
'''

for row in legislators:
    if row[3] == '':
        row[3] = 'M'

'''
#以下仅看下gender中是否只有M，F两种结果。
'''
gender = []
for row in legislators:
    gender.append(row[3])
    
gender = set(gender)
gender


'''
Output
{'F', 'M'}
'''

#---------------------------------------------------------------------------------------------------------------------------

##5. Parsing Birth Years
'''
@author: murphywan
## 这节讲 处理日期型字符串，如：1980-08-30
## 方法：date.split('-')
## 返回：一个元素为string的list
'''

birth_years = []

birthday = []
'''
for row in legislators:
    birthday.append(row[2].split('-'))
    print(birthday)
    birth_years.append(birthday[0])
    #print(birth_years)

#birth_years

以上是第一次尝试，报错。原因是没运行处结果来。
其实真正的原因在于：我把事情搞复杂了，又增加了一个list birthday，然后birth_years变成了list of lists
'''

for row in legislators:
    parts = row[2].split('-')
    birth_years.append(parts[0])

print(birth_years)    


#---------------------------------------------------------------------------------------------------------------------------

## 6. Try/except Blocks

'''
@author: murphywan
## 这节讲 切入正题，Try/except语句
## 出现场景：将一个column的数据类型转换成其他类型时，比如要把year的值从string转化成int
'''

    
try:
    float('Hi, MurphyWan')
except Exception:
    print('Error converting to float.')

#---------------------------------------------------------------------------------------------------------------------------
  
    
## 7. Exception Instances
'''
@author: murphywan
## 这节讲 继续try/except语法，as
1）可以将except的实例赋值给as后面的变量excA。 
2）可以在except语句中调用这个变量excA，即自己的实例

## 方法和举例：
try:
    int('')
except Exception as exc:
    print(type(exc))
'''

try:
    int('Hi, murphywan')
except Exception as exc:
    #Print the type of the Exception instance.
    print(type(exc))
    
    #Convert the Exception instance to a string and print it out.
    print(str(exc))

    
#---------------------------------------------------------------------------------------------------------------------------

##8.The Pass Keyword

'''
@author: murphywan
## 这节讲 继续try/except。想让程序继续执行，而不是每次报错或者导致中断。那么用pass语句。
'''

converted_years = []


'''
以下是第一次尝试，过关，很简单。但是，要扣细节：
#print(birth_years)
for y in birth_years:
    year = y
    try:
        year = int(year)
        print(year)
    except Exception as exc:
        #pass
        print(type(exc))
        print(str(exc))
    converted_years.append(year)

converted_years
'''

for y in birth_years:
    year = y
    try:
        year = int(year)
    except Exception as exc:
        pass
    converted_years.append(year)

converted_years
    
#---------------------------------------------------------------------------------------------------------------------------




