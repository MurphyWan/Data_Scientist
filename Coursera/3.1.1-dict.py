'life is short,you need Python.'.find('you')
Out[49]: 14

my_list = [s.lower() for s in 'Life is short, you need Python.'.split(' ')]

my_list
Out[51]: ['life', 'is', 'short,', 'you', 'need', 'python.']

print('short' in my_list)
False

print(my_list[5])
python.

Keys = ['name','age'];

values = ['Bill',60]

d = dict(Keys = valees)
Traceback (most recent call last):

  File "<ipython-input-56-3587c41225f4>", line 1, in <module>
    d = dict(Keys = valees)

NameError: name 'valees' is not defined


d = dict(Keys = values)

d
Out[58]: {'Keys': ['Bill', 60]}

d = dict(Keys = values)

d = dict(Keys = values)

d
Out[61]: {'Keys': ['Bill', 60]}

Keys = ['name','age'];

values = ['Bill',60]

d = dict(Keys = values)

d
Out[65]: {'Keys': ['Bill', 60]}

print(d)
{'Keys': ['Bill', 60]}

d['name']
Traceback (most recent call last):

  File "<ipython-input-67-881aaaa25d1a>", line 1, in <module>
    d['name']

KeyError: 'name'


# ch3

Keys = ['name','age'];

values = ['Bill',60]

d = dict(Keys = values)

d
Out[72]: {'Keys': ['Bill', 60]}

d['name']
Traceback (most recent call last):

  File "<ipython-input-73-881aaaa25d1a>", line 1, in <module>
    d['name']

KeyError: 'name'


aDict = {}.fromkeys(('murphy','MurphyWan','Bei','Shirley'),30000)

aDict
Out[75]: {'Bei': 30000, 'MurphyWan': 30000, 'Shirley': 30000, 'murphy': 30000}

#以上是用fromkeys把所有key拿出来，赋同样的一个值。

#zip()在生成字典中常常被用到。

#两个list，list1和list2，元素数量一样。可以用dict(zip(list1,list2))来生成字典
