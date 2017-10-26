# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 09:23:03 2017

@author: Administrator
"""

#with open('c:\\test.txt', 'w') as f:
#    f.write('Hello World!')
    
'''
with open('c:\\test.txt') as f :
    p1 = f.read(5)
    p2 = f.read()

print(p1)
print(p2)    
'''

# 文件指针f.tell()
with open('c:\\test.txt') as f :
    p1 = f.read(5)
    p2 = f.read()
    print(f.tell())

print(p1)
print(p2)    
