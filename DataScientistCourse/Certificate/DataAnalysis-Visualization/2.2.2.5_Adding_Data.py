'''
## 这节讲 用ax1.plot(x,y)画两个ax;然后带上data
'''

fig = plt.figure(2)

ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

x1 = unrate['DATE'][:12]
y1 = unrate['VALUE'][:12]
ax1.plot(x1, y1)

x2 = unrate['DATE'][12:24]
y2 = unrate['VALUE'][12:24]
ax2.plot(x2, y2)
