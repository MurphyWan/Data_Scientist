## 1. Introduction to Modules ##

import math

root = math.sqrt(99)
flr = math.floor(89.9)

## 2. Importing Using An Alias ##

# 这节讲导入模块，并使用as给模块取别名
import math as m

root = m.sqrt(33)


## 3. Importing A Specific Object ##

# L2-L01Modules-03-Importing A Specific Object
# 这节讲导入模块中指定的function，而非全部的模块, 用from ... import...

from math import *

root = math.sqrt(1001)



## 4. Variables Within Modules ##

# L2-L01Modules-04-Variables Within Modules
# 这节讲用“.” 方法访问模块中的变量varialbe：module_name.variable_name
# pi = 3.141592653589793 (小数点后面15位哦)

import math

print(math.pi)

pi = math.pi

a = math.sqrt(pi)
b = math.ceil(pi)  #返回x的最大值，大于或等于x的最小整数。如果x不是浮点数，则委托给它x.__ceil__()，该Integral值应该返回一个 值。
c = math.floor(pi)




## 5. The CSV Module ##

# L2-L01Modules-05-The CSV Module
# 这节讲 csv模块。先简单应用，把对象转化成list；最主要使用reader()函数
# 1) import cvs
# 2) open()
# 3) csv.reader(第2步)
# 4) list(第3步)

import csv

nfl = list(csv.reader(open('nfl.csv'))) #我发现，按照上面的列出的步骤，你也可以理清思路，甚至仅用一行写出代码。

# 查看nfl后发现：这是一个list of lists，你懂的！然后，其中的元素都是string。

## 6. Counting How Many Times a Team Won ##

# L2-L01Modules-06-Counting How Many Times a Team Won
# 这节讲 开始简单的分析:某个队伍win的次数

import csv

nfl = list(csv.reader(open('nfl.csv'))) #reader()前面不用遗漏 "csv."
#print(nfl)

patriots_wins = 0
counter = 0 

for row in nfl:
    if "New England Patriots" in row[2]:
        counter = counter + 1
patriots_wins = counter


## 7. Making a Function that Counts Wins ##

# L2-L01Modules-07-Making a Function that Counts Wins
# 这节讲 延续上一节，把某队win 用一个带有一个参数“队伍名”的function(team_name)来写

import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

# Define your function here.

def nlf_wins(team_name):
    
    win_times = 0
    counter =0 
    
    for row in nfl:
        if team_name in row[2]:
            counter += 1
    win_times = counter
    return win_times

cowboys_wins = nlf_wins("Dallas Cowboys")
print(cowboys_wins)

falcons_wins = nlf_wins("Atlanta Falcons")
print(falcons_wins)