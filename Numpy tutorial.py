#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


a = np.array([1,2,3])
print(a)


# In[5]:


b = np.array([[9,8,7],[6,5,4]])
print(b)


# In[6]:


#get dimension
a.ndim


# In[8]:


#get shape
a.shape
b.shape


# In[9]:


#get type
a.dtype


# In[10]:


#get size
a.itemsize


# In[11]:


#get total size
a.nbytes


# In[12]:


a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)


# In[14]:


#get a specific element[r,c]
a[1,-2]


# In[15]:


#get a specific row
a[0,:]


# In[16]:


#get a specific column
a[:,2]


# In[17]:


#getting a little more fancy[startindex:endindex;stepindex]
a[0,1:6:2]


# In[ ]:





# In[18]:


a[1,4] = 20
print(a)


# In[19]:


a[:,2] = [1,2]
print(a)


# In[22]:


b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)


# In[26]:


#get specific element(work outside in)
b[0,1,1]
b[1,1,1]


# In[27]:


#replace
b[:,1,:] = [[9,9,9],[4,4]]


# In[31]:


#all 0s matrix
np.zeros((2,3))


# In[32]:


np.zeros((2,3,5))


# In[33]:


#all is matrix
np.ones((4,2,2), dtype='int32')


# In[34]:


#all other number
np.full((2,2),99)


# In[35]:


#any other number (full like)
np.full_like(a,4)


# In[37]:


#random decimal numbers
np.random.rand(4,2,3)


# In[39]:


#random integer values
np.random.randint(7,size=(3,3))


# In[40]:


np.random.randint(-4,8, size =(3,3))


# In[41]:


#the identity matrix
np.identity(5)


# In[44]:


arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3,axis=0)
print(r1)


# In[65]:


a = np.ones((5,5))
print(a)
a[0,1,1:5] = [[0,0,0]]
print(a)


# In[64]:


output = np.ones((5,5))
print(output)
z = np.zeros((3,3))
z[1,1] = 9
print(z)
output[1:-1,1:-1] = z
print(output)


# In[67]:


#be careful when copying arrays!
a = np.array([1,2,3])
b = a
b[0] = 100
print(a)


# In[68]:


a = np.array([1,2,3])
b = a.copy()
b[0] = 100
print(a)


# In[69]:


#mathematics
a = np.array([1,2,3,4])
print(a)


# In[70]:


a + 2


# In[71]:


a -2


# In[72]:


a * 2


# In[73]:


a / 2


# In[74]:


a **2


# In[75]:


b = ([2,3,4,5])
a + b


# In[76]:


#take the sin
np.cos(a)


# In[79]:


#linear algebra
a = np.ones((2,3))
print(a)
b = np.full((3,2),2)
print(b)
np.matmul(a,b)


# In[81]:


#find the determinant
c = np.identity(3)
np.linalg.det(c)


# In[83]:


#statistic
stats = np.array([[1,2,3],[2,3,4]])
stats


# In[84]:


np.min(stats, axis=1)


# In[85]:


np.max(stats)


# In[86]:


np.sum(stats)


# In[89]:


np.sum(stats,arix=1)


# In[91]:


#reorganizing arrays
before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)
after = before.reshape((4,2))
print(after)


# In[92]:


#vertically stacking vectors
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
np.vstack([v1,v2,v1,v2])


# In[94]:


#horizontal stack
h1 = np.ones((2,4))
h2 = np.zeros((2,2))
np.hstack((h1,h2))


# In[ ]:


#miscellaneous /load data from file


# In[ ]:


filedata = np.genfromtxt('data.txt', delimiter=',')
filedata.astype('int32')
filedata


# In[95]:


#Boolean masking and advANCED INDEXING
filedata > 50


# In[ ]:


filedata[filedata>50]


# In[96]:


#you can index with a list in numpy
a = np.array([1,2,3,4,5,6,7,8,9])
a[[1,2,8]]


# In[ ]:


np.any(filedata > 50, axis=0)


# In[ ]:


np.all(filedata > 50, axis =0)


# In[ ]:


np.all(filedata > 50, axis =1)


# In[ ]:


((filedata > 50) & (filedata < 100))


# In[ ]:


(~(filedata > 50) & (filedata < 100))

