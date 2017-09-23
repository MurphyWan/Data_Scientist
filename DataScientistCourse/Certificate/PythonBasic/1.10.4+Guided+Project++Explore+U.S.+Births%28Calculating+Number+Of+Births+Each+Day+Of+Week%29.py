
# coding: utf-8

# ### This is the Guided Project about Explore U.S. Births

# ### 1.10.1 read file 

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


# ### 1.10.2 将数据转换为嵌套list

# In[4]:


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

    


# In[5]:


cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")
cdc_list


# ### 1.10.03 统计单月出生次数

# In[15]:


def month_births(list_of_lists):
    births_per_month = {} # to store the monthly totals.
    month = []
    births = []
    
    # 这就是一个二维列表+字典的游戏，两个变量的统计。
    # 从二维list（list_of_lists）拿去一维的值lst；然后取出其month列和birhts列元素
    # 然后，看month的值是否已经是字典births_per_month的key了，若是，births_per_month[month]+ births，若不是，births_per_month[month]= births
    # return 字典births_per_month
    for lst in list_of_lists:   
        #month.append(lst[1])   #(错误)挨着排的取list中的月份添加到month 列表中。循环一次取一个
        #births.append(lst[4])  #(错误)挨着排的取list中的出生数量添加到births 列表中。循环一次取一个
        month = lst[1]
        #print(month) # 1)打印 每个lst中的月份
        births = lst[4]
        if month in births_per_month: #判断取出的一个month的值是否已在births_per_month中作为key了
            births_per_month[month] = births_per_month[month]+ births #若yes，则将births的数量加上原先的值，更新赋值
        else:
            births_per_month[month] = births
    #print(month)      # 2)打印 一个数字 12
    return births_per_month


            
        
    


# In[16]:


cdc_month_births = month_births(cdc_list)
cdc_month_births


# ### 1.10.04 统计在星期几出生的次数

# In[20]:


def dow_births(data):
    births_per_dow = {}
    
    for lst in data:
        day_of_week = lst[3] # 观察了xls表格，星期几在第四列，所以index为3
        births = lst[4]
        
        if day_of_week in births_per_dow:
            births_per_dow[day_of_week] = births_per_dow[day_of_week] + births
        else:
            births_per_dow[day_of_week] = births
    return births_per_dow

cdc_list = read_csv("US_births_1994-2003_CDC_NCHS.csv")


# In[21]:


cdc_day_births = dow_births(cdc_list)
cdc_day_births

