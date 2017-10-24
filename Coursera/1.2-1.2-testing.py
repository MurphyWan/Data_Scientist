# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 20:46:43 2017

@author: MurphyWan
"""

#1．编写一个输入分数，输出分数等级的程序，具体为：
score = int(input('请输入一个分数（0-100之间）：'))

if 90 <= score <= 100:
    print('A')
elif 70 <= score <= 89:
    print('B')
elif 60 <= score <= 69:
    print('C')
elif 0<= score <= 59:
    print('D')
else:
    print('others Invalid score')    
    
    

#2. 验证命题：如果一个三位整数是37的倍数，则这个整数循环左移后得到的另两个3位数也是37的倍数。（注意验证命题的结果输出方式，只要输出命题为真还是假即可，而非每一个三位数都有一个真假的输出）



#3.验证哥德巴赫猜想之一：2000以内的正偶数（大于等于4）都能够分解为两个质数之和。每个偶数表达成形如：4=2+2的形式，输出时每行显示6个式子。



#4. 编写一个程序，让用户输入苹果个数和单价，然后计算出价格总额。
while True:
    try:
        count = int(input('你要买几个苹果:'))
        unit_price = int(input('输入苹果单价：'))
        price = count * unit_price
        print('总价是：', price)
    except ValueError as error:
        print(error)
        print('Error,please enter a numeric one:')
    
