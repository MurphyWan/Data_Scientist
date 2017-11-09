'''
## Formatting And Spacing
## 这节讲 用fig = plt.figure(figsize=(width, height))来确定图片大小和纵横比,width和height的单位是英寸;
'''

fig = plt.figure(figsize=(12,5)) # 填上figsize=(12,5)即可
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
ax1.plot(unrate[0:12]['DATE'], unrate[0:12]['VALUE'])
ax1.set_title('Monthly Unemployment Rate, 1948')
ax2.plot(unrate[12:24]['DATE'], unrate[12:24]['VALUE'])
ax2.set_title('Monthly Unemployment Rate, 1949')
plt.show()
