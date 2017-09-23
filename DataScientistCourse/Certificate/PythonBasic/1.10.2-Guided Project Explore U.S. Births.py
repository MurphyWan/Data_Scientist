
# coding: utf-8

# ### This is the Guided Project about Explore U.S. Births

# #### read file 

# In[7]:


file = open("US_births_1994-2003_CDC_NCHS.csv", 'r')
data = file.read()
split_data = data.split('\n')
split_data[:10]


# In[17]:


def read_csv(file_name):
    file = open(file_name, 'r')
    data = file.read()
    split_data = data.split('\n') #用split() + \n 将字符串分行
    string_list = split_data[1:]  #剔除header row
    final_list = []
    for row in string_list:
        #print(row)
        string_fields = row.split(',')  # 用split() + ',' 以逗号为间隔将字符串分开       
        final_list.append(string_fields) #将每一个分开的字符串list添加到final_list list中
        #print(string_fields)
        #for each in string_fields:
        #    int_fields.append(int(each))
        #    #print(int_fields)
    return final_list


# In[18]:


cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")
cdc_list[0:10]


# ### 将数据转换为嵌套list

# In[22]:


def read_csv(file_name):
    data = open(file_name, 'r').read()
    string_list = data.split('\n')[1:]
    final_list = []
    for row in string_list:
        int_fields = []
        string_fields = row.split(',')  #用split()+','把逗号分隔的“stringA","stringB",...,"stringN"，变成了lists,即[listA],[listB],...,[listN]
        
        for each in string_fields:      #each 是上面lists中的每个list；for循环的作用是将名为string_fields的list的每个元素由string变int
            int_fields.append(int(each))#将每个each list中的元素变为int，然后添加到int_fields list中去。
        #print(int_fields)  #打印结果是，显示所有lists，且list与list之间没有逗号","且list之间分行显示。
        final_list.append(int_fields)
    return final_list

    


# In[24]:


cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")
cdc_list

