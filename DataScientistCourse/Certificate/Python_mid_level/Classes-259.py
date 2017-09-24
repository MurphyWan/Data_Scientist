## 2. Defining the Dataset Class ##

# L2-L02Class-02-Defining the Dataset Class
# 这节讲 如何定义一个类class
# 这节把 之前没有看太明白的__init__()和用dot notation访问一个类的属性（new_dataset.type）看明白了。

class Dataset:
    def __init__(self):
        self.type = "csv"
        
dataset = Dataset() # 如何为一个类创建“实例”？ 很简单：“类名+()”赋值即可。
print(dataset.type)

        
        
        



## 3. Passing Additional Arguments to the Initializer ##

# L2-L02Class-03-Passing Additional Arguments to the Initializer
# 这节讲 为__init__()方法添加新的参数，以及配套的变量
# 1)创建类的实例 nlf-dataset；并自带类参数；
# 2)通过 “类实例名.参数”访问 __init__(self, data)中的data变量
# 3)这样做的好处是什么？我没太想明白。（下一节给出答案：使用self变量的好处是我们可以从我们定义的任何实例方法引用它  ）

import csv

class Dataset:
    def __init__(self,data):
        self.type = "csv"
#------------以上为题目原文------------------

class Dataset:
    def __init__(self,data):
        self.type = "csv"
        self.data = data
        
nfl_data = list(csv.reader(open("nfl.csv")))
#Instant = Dataset(self,nfl_data)
nfl_dataset = Dataset(nfl_data) #1）创建类实例。如何把结果赋值给nfl_dataset？
#print(nfl_dataset)
dataset_data = nfl_dataset.data #2）通过 “类实例名.参数或者说变量”访问 __init__(self, data)中的data变量
#print(dataset_data)

## 4. Adding Additional Behavior ##

# L2-L02Class-04-Adding Additional Behavior
# 这节讲 为类增加新的行为（方法）：打印数据的前十行
# 调用类实例方法：self.方法名() 或者 实例名.方法名()
# 注意点：
  #1）定义类方法的参数是，第一个务必要写self！ 这里print_data(self, num_rows)
  #2）__init__()方法中的参数，这里指变量data，已经定义过了，所以，新方法print_data里面可以直接使用。

class Dataset:
    def __init__(self, data):
        self.data = data
        
    # Your method goes here
#---------以上以为原题内容----------------------------------------------------------
    def print_data(self,num_rows):   #1）定义类方法的参数是，第一个务必要写self！
        print(self.data[0:num_rows]) #2）__init__()方法中的参数，这里指变量data，已经定义过了，所以，新方法print_data里面可以直接使用。

#print(nfl_data)        

nfl_dataset = Dataset(nfl_data) #类实例化

nfl_dataset.print_data(5)


## 5. Enhancing the Initializer ##

# L2-L02Class-05-Enhancing the Initializer
# 这节讲 利用类初始化（instantiation）方法只能被调用only一次的特性，设置仅在初始化期间，只可以调用一次的方法
import csv


class Dataset:
    def __init__(self, data):
        self.data = data

nfl_dataset = Dataset(nfl_data)

"""
#----以下为第一次的写法（增加一个方法extract_header()）：
class Dataset:
    def __init__(self, data):
        self.data = data
    
    def extract_header(self):
        self.header = self.data[0]
"""

"""
#----以下为第二次的写法（增加一个方法extract_header()）：
class Dataset:
    def __init__(self, data):
        self.data = data
    
    def extract_header(self):
        self.header = self.data[0]
        self.data = self.data[1:]
"""

"""
#----以下为第三次的写法（参考了答案,并没有增加extract_header()方法）：
class Dataset:
    def __init__(self, data):
        self.data = data[1:]
        self.header = data[0]
"""


#----以下为第四次的写法（参考了答案,但依然增加了extract_header()方法）(Done)
class Dataset:
    def __init__(self, data):
        self.data = data
    
    def extract_header(self):
        self.header = self.data[0]
        #self.data = data[1:]
        return self.header
        
#nfl_data = list(csv.reader(open("nfl.csv")))        

nfl_dataset = Dataset(nfl_data)
nfl_header = nfl_dataset.extract_header()
print(nfl_header)


## 6. Grabbing Column Data ##

# L2-L02Class-06-Grabbing Column Data
# 这节讲 【获取列的数据】，包括获取index的值
# 这节在做的时候虽然可以看到题目的字面意思，但是感觉完全难以开展！！！百思不得其解，所以看了提示和答案。
# 根据答案第20行 if label == element: 可推测：lebel是指某一列的value
"""
# 关键步骤：
# 1）随便给一个输入值（label），看其是否在表头中出现？
# 2）如果no，返回None
# 3）如果yes，即在的话（用for + enumerate(表头)枚举），取其label=element这个值对应的index值
# 4）去column数据，用for row in self.data\ column.append(row[index])
"""
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
        
    # Add your method here.
    def column(self,label):    # 这里不要忘记：写上self！！！
        if label not in self.header:  
            return None
        
        index = 0 
        for idx, element in enumerate(self.header): 
            #查看enumerate功能：http://book.pythontips.com/en/latest/enumerate.html
            #enumerate(list, number) 这里的number是从几开始，如果number= 1 ，则1 year ；2week；3 winner
            #print(idx,element)  #通过这个print，可以知道：enumerate把self.header表头有哪些字段枚举了一遍。
            #一个问题：这里一定要用 idx,element这两个变量名吗？还是其他都可以？（  ）
            #打印结果如下：
            # 0 year
            # 1 week
            # 2 winner
            # 3 loser
            # （A）结论1：idx其实是表头字段对应的索引index值，就是column的索引值。
            if label == element:
                index = idx
        
        column = []
        for row in self.data:
            column.append(row[index]) #（B）根据结论1，所以row[index]就是相应记录的列的value。
        return column
    
nfl_dataset = Dataset(nfl_data)
year_column = nfl_dataset.column('year') #（C）这里传入'year'，所以，枚举返回index 为0 .
player_column = nfl_dataset.column('player')


## 7. Count Unique Method ##

# L2-L02Class-07-Count Unique Method
# 这节讲 set()获取list中的唯一值，就是一堆相同的value不重复显示，只显示一个。

class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
    
    def column(self, label):
        if label not in self.header:
            return None
        
        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx
        
        column = []
        for row in self.data:
            column.append(row[index])
        return column
# 以上都是原文------------------------------------------------------    
    # Add your count unique method here
'''
# 第一次尝试：没看清题目，要的是关于唯一年份的个数，结果算出来的是5个具体的年份。    
    def count_unique(self, label):
        result = self.column(label)
        unique_result = set(result)
        return unique_result
        
nfl_dataset = Dataset(nfl_data)
total_years = len(nfl_dataset.count_unique("year"))
''' 
'''
    def count_unique(self, label):
        result = set(self.column(label))
        unique_result = len(result)
        reutrn unique_result
'''
class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
    
    def column(self, label):
        if label not in self.header:
            return None
        
        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx
        
        column = []
        for row in self.data:
            column.append(row[index])
        return column
    
    def count_unique(self, label):
        result = set(self.column(label))
        count_result = len(result)
        return count_result

nfl_dataset = Dataset(nfl_data)
total_years = nfl_dataset.count_unique("year")

## 8. Make Objects Human Readable ##

# L2-L02Class-08-Make Objects Human Readable
# 这节讲 


class Dataset:
    def __init__(self, data):
        self.header = data[0]
        self.data = data[1:]
    
#------------------------------------------    
    # Add the special method here
    def __str__(self):
        return self.data[:10]
    
#------------------------------------------
    def column(self, label):
        if label not in self.header:
            return None
        
        index = 0
        for idx, element in enumerate(self.header):
            if label == element:
                index = idx
        
        column = []
        for row in self.data:
            column.append(row[index])
        return column
    
        
    def count_unique(self, label):
        unique_results = set(self.column(label))
        count = len(unique_results)
        return count

nfl_dataset = Dataset(nfl_data)
nfl_dataset.__str__()