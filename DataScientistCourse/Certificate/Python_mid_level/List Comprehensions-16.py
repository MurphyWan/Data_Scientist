## 2. Enumerate ##

'''
## List Comprehensions | 01 The Data Set
## 这节讲 string型的list | enumerate()函数 | 和2变量的for循环。有了for中的i，就可以关联两个list中，对应[i]位置的元素了。
## 举例如下：
for i, animal in enumerate(animals):
    print("Animal Index")  ## label
    print(i)
    print("Animal") ## label
    print(animal)

i： 相当于string list的index，从0开始；
animal：就是animals中的每个元素
i和animal是关联的，一一对应的。

'''

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]

for i, ship in enumerate(ships):
    #print("ship")
    print(ship)
    #print('car')
    print(cars[i])


#---------------------------------------------------
'''
## List Comprehensions | 03 Adding Columns
## 这节讲 还是enumerate()，给二维list增加列。把一个1D list中的所有元素添加到另一个2D list of lists中的每一维中。

for example:
door_count = [4, 4]
cars = [
        ["black", "honda", "accord"],
        ["red", "toyota", "corolla"]
       ]

for i, car in enumerate(cars):
    car.append(door_count[i])

#--------------------------------以下是讲解
第一次循环：
i= 0 
car = ['black','honda','accord']
car.append(door_count[0]) --> = ['black','honda','accrod','4'] # list必须元素是同一种类型。

第二次循环：
i= 1 
car = ['black','honda','accord','0']
car.append(door_count[1]) --> =  ['black','honda','accrod','4','4']

第三次循环：
第三次循环，是怎么开始的？
door_count[i]，这点很重要。door_count作为list只有2个元素，所以，index就到1结束了。
具体判断，i=2，在door_count这里超出下标。然后，car这边就进入下一轮循环了，此时car = cars[2]
i= 0
car = ['red','toyota','corolla']
car.append(door_count[0])--> = ['red','toyota','corolla','4']

第四次循环：
i= 1
car = ['red','toyota','corolla','4']
car.append(door_count[1])--> = ['red','toyota','corolla','4','4']

第五次循环：
i = 2，突破door_count的下标。结束。所以第五次循环，循环体的内容并没有执行。

#----------------------------------------------------------------
In the code above, we:

Use the enumerate() function to loop across each item in cars.
Find the corresponding value in door_count that has the index i (the same index as the current item in cars).
Add the value in door_count with index i to car.
After the code runs, each row in cars will have a door_count column.

'''

things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]

for i , thing in enumerate(things):
    thing.append(trees[i])
    
#-----------------------------------------------------------------


'''
## List Comprehensions 列表解析式 | 04. List Comprehensions
## 作用：用一个现成的list生成新的list
## 注意：用在列表解析式中的for循环最后是没有冒号的“：”

for example:
animal_lengths = [len(animal) for animal in animals]
'''

apple_prices = [100, 101, 102, 105]

'''
#------------第一次尝试-------------------
apple_prices_doubled = apple_prices * 2
apple_prices_lowered = apple_prices - 100
#结果失败。numpy的ndarray数组应该可以这样操作。
'''
apple_prices_doubled = [n*2 for n in apple_prices]
apple_prices_lowered = [m-100 for m in apple_prices]



#-------------------------------------------------------------------

'''
## List Comprehensions 列表解析式 | 05. Counting Female Names

'''

name_counts = {}
'''
# 第一次尝试，结果错误。原因在于，取了list而不是一个具体的元素进行比较。
for each in legislators:
    if legislators['gender'] == 'F' and legislators['year'] > 1940:
        name = each[1]
        if name in name_counts:
            name_counts[name]  += 1
        else:
            name_counts[name] = 1
name_counts

'''
#legislators

for row in legislators:
    gender = row[3]    #记住，一定是取当前行的元素，而不是循环legislators中的一列。
    year = row[7]      #同上。
    name = row[1]
    if gender == "F" and year > 1940:
        
        if name in name_counts:
            name_counts[name] = name_counts[name] + 1
        else:
            name_counts[name] = 1

#---------------------------------------------------------------------------------------

#-- 6. None---

'''python
Let's say we're trying to find the maximum value in a list. We might write some code that looks like this:

values = [50, 80, 100]
max_value = 0
for i in values:
    if i > max_value:
        max_value = i
We set max_value to a low value so that everything's greater than it. But what if we changed the values list slightly?

values = [-50, -80, -100]
max_value = 0
for i in values:
    if i > max_value:
        max_value = i
In the above scenario, max_value is 0 when the loop finishes. This is wrong, because 0 isn't in values; it's just a placeholder we used to initialize max_value.

We can resolve this kind of issue using the None object, which has a special data type called NoneType.

The None object indicates that the variable has no value. Rather than using the normal double equals sign (==) to check whether a value equals None, we use the variable is None syntax.

The is comparison operator checks for object equality. Using is instead of == prevents some custom classes from resolving to True when compared with None. We'll explore how to use operators with the None object in greater depth during a later mission. For now, let's see what the variable is None syntax looks like:

values = [-50, -80, -100]
max_value = None
for i in values:
    if max_value is None or i > max_value:
        max_value = i
In the example above, we:

Initialize max_value to None.
Loop through each item in values.
Check whether max_value equals None using the max_value is None syntax.
If max_value equals None, or if i > max_value, then we assign the value of i to max_value.
At the end of the loop, max_value will equal -50, which is the largest value in values.
'''

#------------------------------------------------------------------------------------------

'''
## List Comprehensions | 07. Comparing with None

'''

values = [None, 10, 20, 30, None, 50]
checks = []

'''
## 第一次尝试，理解错题意。应该是返回所有比较元素的布尔值。
for value in values:
    if value is not None and value > 30:
        checks.append(value)
'''

checks = [x is not None and x >30 for x in values]

'''
output:
[False, False, False, False, False, True]
'''

#-----------------------------------------------------------------------------------------

'''
## List Comprehensions | 08. Highest Female Name Count

'''

'''
name_counts is a dictionary where the keys are female first names from legislators, and the values are the number of times the names occured after 1940.

In order to extract the most common names from this dictionary, we need to determine the highest totals in name_counts. Once we know the totals, we can find the keys for them.

We can iterate through all of the keys in a dictionary like this:
'''
'''python
fruits = {
        "apple": 2,
        "orange": 5,
        "melon": 10
    }

for fruit in fruits:
    rating = fruits[fruit]
'''
'''
In the loop above, we iterate through each key in fruits. We can access the corresponding value using fruits[fruit].

Let's identify the highest totals in the next exercise.
'''

max_value = None

for key in name_counts:
    count = name_counts[key]
    if max_value is None or count > max_value:
        max_value = count
