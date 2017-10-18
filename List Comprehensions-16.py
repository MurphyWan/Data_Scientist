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




## 3. Adding Columns ##

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
    



