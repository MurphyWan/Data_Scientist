
# coding: utf-8

# # 用Python进行数据分析

# ## Ch4 Numpy基础，数组和矢量计算

# ### P95 花式索引

# In[2]:

import numpy as np


# In[3]:

arr = np.empty((8,4))


# In[4]:

for i in range(8):
    arr[i] = i


# In[5]:

arr


# In[6]:

arr[[4,3,0,6]]


# In[7]:

arr[[-3, -5, -7]]


# In[8]:

arr = np.arange(32).reshape((8,4))


# In[9]:

arr


# In[10]:

arr[[1,5,7,2],[0,3,1,2]]


# In[11]:

arr[[1,5,7,2]][:,[0,3,1,2]]


# In[12]:

arr[np.ix_([1,5,7,2],[0,3,1,2])]


# ### P97 数组转置和轴对换

# In[13]:

arr = np.arange(15).reshape((3,5))


# In[14]:

arr


# In[15]:

arr.T


# In[16]:

arr = np.random.randn(6,3)


# In[17]:

np.dot(arr.T, arr)


# In[18]:

arr = np.arange(16).reshape((2,2,4))


# #### 2,    2,   4 ， 首2表示二维，次2及4，表示2×4的矩阵，即次2表示行，4表示列
# #### 2[0],2[1],4[2]
# #### 角标是0，1，2

# In[19]:

arr


# #### 下面这个转置比较搞脑子
# #### 本来角标是（0，1，2），现在变成（1，0，2），0与1的位置互换了。
# #### 原本8的索引是 （1，0，0），现在要变成（0，1，0），第三个位置的0不动，前面的0和1位置互换

# In[20]:

arr.transpose((1,0,2))


# #### swapaxes（d1,d2），d1和d2两个维度互换，那么不过写0和1，还是1和0，结果是一样的，都是0和1互换
# #### 因此swapaxes(0,1)和swapaxes(1,0)结果结果一致
# #### swapaxes(1，2)，1和2互换，则是行列互换了。

# In[21]:

arr.swapaxes(1,2)


# In[22]:

arr.swapaxes(0,1)


# In[23]:

arr.swapaxes(1,0)


# In[24]:

arr


# In[ ]:



