'''
## 这节讲 pyplot.bar() or Axes.bar()画柱图；Axes.bar()有2个必要参数，和1个可选参数。必填：left和heigt，可选是width
## 方法是：
plt.bar(*left, *height, *width)
'''

import matplotlib.pyplot as plt
from numpy import arange
num_cols = ['RT_user_norm', 'Metacritic_user_nom', 'IMDB_norm', 'Fandango_Ratingvalue', 'Fandango_Stars']

#定义bar()中2个必须的参数，left和height
bar_left = arange(5) + 0.75
bar_heights = norm_reviews[num_cols].iloc[0].values


#定义bar()中1个可选参数，width
plt.bar(bar_left, bar_heights, width  = 0.5)
plt.show()
