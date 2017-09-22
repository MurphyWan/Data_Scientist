
# coding: utf-8

# In[1]:


f = open('births.csv', 'r')
text = f.read()
text





# In[2]:


split_txt = text.split('\n')
split_txt


# In[3]:


list_of_lists = []
for row in split_txt:
    split_data = row.split(',')
    list_of_lists.append(split_data)

list_of_lists


# In[12]:


days_counts  = {}
new_list = list_of_lists[1:]

day_of_week = []
births = []
for line in new_list:
    day_of_week.append(int(line[3]))
    births.append(int(line[4]))

day_of_week


# In[9]:


births


# ## below is the dicitionary of days_counts  contaning the total number of births for each unique day of the week
# 
# ### I use nested *for* loop to deal with the values of unique day_of_week accociated values of total number of births.

# In[15]:


for days_item in day_of_week:
    for births_item in day_of_week:
        if days_item in days_counts:
            days_counts[days_item] = days_counts[days_item] + 1
            if births_item in days_counts:
                days_counts[births_item] = days_counts[births_item] + 1
            else:
                days_counts[births_item] = 1
        else:
            days_counts[days_item] = 1
            if births_item in days_counts:
                days_counts[births_item] = days_counts[births_item] + 1
            else:
                days_counts[births_item] = 1



# In[16]:


days_counts

