# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 20:11:24 2017

@author: Administrator
"""
'''
# 
def ask(prompt = "Do you like Python? ", hint = "yes or no"):
     while True:
          answer = input(prompt)
          if  answer.lower() in ('y', 'yes'):
              print("Thank you")
              return True
          if  answer.lower()  in  ('n', 'no') :
              print("why not")
              return False
          else:
              print(hint)


ask("Do you like Python? ")
'''
 
'''

i = [1,2,3,4]
print('01 i.insert(2,-1)' , i.insert(2,-1))

i = [1,2,3,4]
i.pop()
print(r'02 i.index(3)', i.index(3))

i = [1,2,3,4]
i.reverse()
print('03 i[1] = ', i[1])

i = [1,2,3,4]
i.pop(1)
print('04 i.pop(1) = ', i)
'''

'''
print((1,2,3,4)< (1,2,4))
'''

'''
alist = [1,3,2,4]
btuple = (1,3,2,4)


print(r'01 sorted(alist) =', sorted(alist))
print(r'02 sorted(btuple) =', sorted(btuple))
print(r'03 btuple.sort() =', btuple.sort())  #这条语句报错
print(r'04 alist.sort() = ', alist.sort())

#output of above as belowing:
01 sorted(alist) = [1, 2, 3, 4]
02 sorted(btuple) = [1, 2, 3, 4]
04 alist.sort() =  None

'''

