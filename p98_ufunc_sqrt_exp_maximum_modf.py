
# coding: utf-8

# In[24]:

import numpy as np
import numpy.matlib


# In[25]:

arr = np.arange(10)


# In[26]:

arr


# In[27]:

np.sqrt(arr)


# In[28]:

np.exp(arr)


# In[29]:

x = np.matlib.randn(8)


# In[31]:

y = np.matlib.randn(8)


# In[32]:

x


# In[33]:

y


# In[34]:

np.maximum(x,y)


# In[35]:

arr = np.matlib.randn(7) * 5


# In[36]:

np.modf(arr)


# In[ ]:



