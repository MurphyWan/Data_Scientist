
# coding: utf-8

# # 用Python进行数据分析

# ## Ch4 Numpy基础，数组和矢量计算

# ### P95 花式索引

# In[1]:

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


# In[9]:

arr = np.arange(32).reshape((8,4))


# In[10]:

arr


# In[11]:

arr[[1,5,7,2],[0,3,1,2]]


# In[12]:

arr[[1,5,7,2]][:,[0,3,1,2]]


# In[19]:

arr[np.ix_([1,5,7,2],[0,3,1,2])]


# ### P97 数组转置和轴对换

# In[20]:

arr = np.arange(15).reshape((3,5))


# In[21]:

arr


# In[22]:

arr.T


# In[23]:

arr = np.random.randn(6,3)


# In[24]:

np.dot(arr.T, arr)


# In[25]:

arr = np.arange(16).reshape((2,2,4))


# In[26]:

arr


# #### 下面这个转置比较搞脑子

# In[27]:

arr.transpose((1,0,2))


# In[29]:

arr.swapaxes(1,2)


# In[ ]:



