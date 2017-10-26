# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 10:18:03 2017

@author: Administrator
"""

'''
import requests

re = requests.get('http://www.jianshu.com/u/d23589a1659b')
print(re)
print(re.text)
'''


import requests

re = requests.get('https://mail.google.com/mail/u/0/?ui=2&ik=71ed725f21&view=lg&msg=15f4bb1fcd9e7222')
print(re.text)