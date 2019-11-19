#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


my_arr = np.arange(1000000)


# In[3]:


my_list = list(range(1000000))


# In[4]:


get_ipython().run_line_magic('time', 'for _ in range(10) : my_arr2 = my_arr * 2')


# In[5]:


get_ipython().run_line_magic('time', 'for _ in range(10) : my_list2 = [x * 2 for x in my_list]')


# In[7]:


data = np.random.randn(2,3)
data


# In[8]:


data * 10


# In[9]:


data + data


# In[10]:


data.shape


# In[11]:


data.dtype


# In[12]:


data1 = [6, 7.5, 8,0.1]
arr1 = np.array(data1)
arr1


# In[13]:


data2 = [[1,2,3,4],[5,6,7,8]]
arr2 = np.array(data2)
arr2


# In[14]:


arr2.size


# In[15]:


arr2.shape


# In[16]:


arr2.ndim


# In[17]:


arr1.dtype


# In[18]:


arr2.dtype


# In[19]:


np.zeros(10)


# In[20]:


np.ones(10)


# In[22]:


np.zeros((3,6))


# In[23]:


np.ones((2,4))


# In[24]:


np.empty((2,3,3))


# In[25]:


np.arange(15)


# In[27]:


list_z = [99,98,95,91,12]
lista_z2 =np.array(list_z)
lista_z2


# In[31]:


lista_z2.asarra


# In[32]:


zeta = (1,3,5,7,8)
np_zeta = np.asarray(zeta)
np_zeta


# In[44]:


x = np.arange(5)
x


# In[42]:


y = np.arange(10,-1)
y


# In[46]:


df = np.ones_like ((6,3))
df


# In[48]:


df = np.zeros((2,5))
df


# In[51]:


df2 = np.ones_like(df)
df2


# In[52]:


se = np.arange(7)
se


# In[57]:


se_flaot = se.astype(np.float64)
se_flaot


# In[59]:


arr = np.array([[1,2,3],[4,5,6]])
arr


# In[60]:


arr * arr


# In[61]:


arr - arr


# In[62]:


1 / arr


# In[63]:


arr ** 0.5


# In[64]:


arr2 = np.array ([[0,4,5],[1,9,0]])
arr2


# In[65]:


arr2 > arr


# In[66]:


arr


# In[70]:


arr[1]


# In[71]:


arr[1][2]


# In[76]:


arr[0][0] <= arr[1][0]


# In[78]:


arr[:1]


# In[80]:


arr[:1] = 8
arr


# In[81]:


nv = arr[:1].copy()
nv


# In[82]:


arr[0,2]


# In[83]:


arr[0][2]


# In[84]:


arr[1,:2]


# In[86]:


arr[1,:2]


# In[87]:


arr[:1,2]


# In[89]:


names = np.array(['bob','john','will','rod','will','tom','bob'])
names


# In[91]:


names == 'bob'


# In[90]:


data = np.random.randn(7,4)
data


# In[92]:


data[names == 'bob']


# In[93]:


data[names == 'bob',2]


# In[94]:


data[names == 'bob',2:]


# In[95]:


data[names == 'bob',3]


# In[96]:


names != 'bob'


# In[97]:


data[~(names == 'bob')]


# In[99]:


mask = (names == 'bob') | (names == 'will')
mask


# In[100]:


data[mask]


# In[101]:


mask = (names == 'bob') & (names == 'will')
mask


# In[104]:


data[data < 0 ] = 0
data


# In[110]:


data[names != 'tom'] = 7
data


# In[114]:


arr = np.empty((8,4))
for i in range (8):
    arr[i] = i
arr


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




