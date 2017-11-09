'''
## Comparing Across More Years
## 这节讲 用for来画1个figure中多个add_subplot图
'''


fig = plt.figure(figsize=(12,12))
'''
ax1 = fig.add_subplot(5,1,1)
ax2 = fig.add_subplot(5,1,2)
ax3 = fig.add_subplot(5,1,3)
ax4 = fig.add_subplot(5,1,4)
ax5 = fig.add_subplot(5,1,5)
'''

for i in [1,2,3,4,5]:
    ax = fig.add_subplot(5,1,i)
    ax.plot(unrate['DATE'][12*(i-1):12*i], unrate['VALUE'][12*(i-1):12*i])

plt.show()


'''
虽然觉得自己写的代码远比答案的更加精简，只是读起来没有它方便。标准答案定义每一步都很清晰。
另外，
1、我一开始用笨办法，没考虑用for 循环；
2、ax[i]的原始想法比较扯，其实每次循环，ax都可以在该次循环中画完图，所以只要赋值于ax而不是ax[i]就行。
'''
