#### this folder  contains some python files which are the answers of python pandas practise from the website of Coursera.org

'''python
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
'''
