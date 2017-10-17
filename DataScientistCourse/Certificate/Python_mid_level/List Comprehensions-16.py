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


