help(math.ceil)
Help on built-in function ceil in module math:

ceil(...)
    ceil(x)
    
    Return the ceiling of x as an Integral.
    This is the smallest integer >= x.


math.ceil(4.6)
Out[11]: 5

math.floor(4.6)
Out[12]: 4

#ceil()向上取整

#floor()向下取整

import random

print(random.choice(['霸刀总裁风','冷艳高贵风','扎心老铁风','人来疯']))
冷艳高贵风

from datetime import date

date.today()
Out[18]: datetime.date(2017, 10, 24)

from datetime import time

datetime.time()
Traceback (most recent call last):

  File "<ipython-input-20-7a536f562689>", line 1, in <module>
    datetime.time()

NameError: name 'datetime' is not defined


from datetime import time

tm = time(21,50,59)

print(tm)
21:50:59

from datetime import datetime

dt = datetime.now()

dt
Out[26]: datetime.datetime(2017, 10, 24, 21, 52, 37, 29477)

print(dt.strftime('%A, %B, %D, %Y %H:%M'))
Tuesday, October, 10/24/17, 2017 21:52

print(dt.strftime('%a, %b, %d, %Y %H:%M'))
Tue, Oct, 24, 2017 21:52

dt = datetime(2017,10,24, 21,59)

dt
Out[30]: datetime.datetime(2017, 10, 24, 21, 59)

print(dt)
2017-10-24 21:59:00

#把这个时间转成时间戳 timestamp

ts = dt.timestamp()

ts
Out[34]: 1508853540.0

#把时间戳转成本地时间和日期

print(datetime.fromtimestamp(ts))
2017-10-24 21:59:00

#用timestamp统一全球所有计算机的时间。从1970年1月1日0时0时区开始计算
