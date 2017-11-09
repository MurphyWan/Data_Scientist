'''
## Comparing Across More Years
## 这节讲 用unrate['DATE'].dt.month来提取DATE(yyyy/mm/dd)中的月份;然后画折线图
'''


unrate['MONTH'] = unrate['DATE'].dt.month

'''
## 错误：我把figure分成了上下两块。修正：将add_subplot(2,1,1)改成1,1,1即可
fig = plt.figure(figsize=(6,3))

ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,1)

ax1.plot(unrate['MONTH'][:12],unrate['VALUE'][:12], c = 'red' )
ax2.plot(unrate['MONTH'][12:24],unrate['VALUE'][12:24], c = 'blue' )
plt.show()
'''

fig = plt.figure(figsize=(6,3))

ax1 = fig.add_subplot(1,1,1)
ax2 = fig.add_subplot(1,1,1)

ax1.plot(unrate['MONTH'][:12],unrate['VALUE'][:12], c = 'red' )
ax2.plot(unrate['MONTH'][12:24],unrate['VALUE'][12:24], c = 'blue' )
plt.show()

'''
另外，在一个figure画线，就不需要多此一举，在用add_subplot了，直接plt.plot画即可。这点请参考标准答案。
'''
