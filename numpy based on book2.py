#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[7]:


arr = np.empty((8,4))
arr
for i in range(8):
    arr[i] = i
arr


# In[9]:


arr[[4,3,0,6]]


# In[10]:


arr[[-7,-5,-3]]


# In[11]:


arr = np.arange(32).reshape((8,4))
arr


# In[12]:


arr[[1,5,7,2],[0,3,1,2]]


# In[15]:


arr[[1,5,7,2]][:,[0,3,1,2]]


# In[16]:


arr = np.arange(15).reshape((3,5))
arr


# In[17]:


arr.T


# In[19]:


arr = np.random.randn(6,3)
arr


# In[20]:


np.dot(arr.T,arr)


# In[22]:


arr = np.arange(16).reshape((2,2,4))
arr


# In[24]:


arr.transpose((1,0,2))


# In[25]:


arr.swapaxes(1,2)


# In[28]:


arr = np.arange(10)
arr


# In[29]:


np.sqrt(arr)


# In[30]:


np.exp(arr)


# In[31]:


x = np.random.randn(8)
y = np.random.randn(8)
x


# In[32]:


y


# In[33]:


np.maximum(x,y)


# In[34]:


arr = np.random.randn(7) * 5
arr


# In[36]:


remainder, whole_part = np.modf(arr)
remainder


# In[37]:


whole_part


# In[38]:


np.sqrt(arr)


# In[39]:


np.sqrt(arr,arr)


# In[40]:


arr


# In[41]:


points = np.arange(-5,5,0.01)


# In[42]:


xs, ys = np.meshgrid(points,points)
ys


# In[43]:


z = np.sqrt(xs ** 2 + ys ** 2)
z


# In[44]:


xarr = np.array([1.1,1.2,1.3,1.4,1.5])
yarr = np.array([2.1,2.2,2.3,2.4,2.5])
cond = np.array([True,False,True,True,False])


# In[45]:


result = [(x if c else y)
for x, y, c in zip(xarr, yarr, cond)]
result


# In[46]:


result = np.where (cond, xarr, yarr)
result


# In[47]:


arr = np.random.randn(4,4)
arr


# In[48]:


arr > 0


# In[49]:


np.where(arr > 0, 2, -2)


# In[50]:


np.where(arr > 0, 2, arr)


# In[51]:


arr = np.random.randn(5,4)
arr


# In[52]:


arr.mean()


# In[53]:


np.mean(arr)


# In[54]:


arr.sum()


# In[55]:


arr.mean(axis=1)


# In[56]:


arr.mean(axis=0)


# In[57]:


arr.sum(axis=0)


# In[58]:


arr = np.array([0,1,2,3,4,5,6,7])
arr.cumsum()


# 

# In[59]:


arr = np.array([[0,1,2],[3,4,5],[6,7,8]])
arr


# In[60]:


arr.cumsum(axis=0)


# In[61]:


arr.cumprod(axis=1)


# In[62]:


arr = np.random.randn(100)
arr


# In[63]:


(arr > 0).sum()


# In[64]:


bools = np.array([False,False,True,False])
bools.any()


# In[65]:


bools.all()


# In[70]:


arr = np.random.randn(6)
arr


# In[72]:


arr.sort()
arr


# In[73]:


arr = np.random.randn(5,3)
arr


# In[75]:


arr.sort(1)
arr


# In[77]:


large_arr = np.random.randn(1000)
large_arr.sort()
large_arr[int(0.05 * len(large_arr))]


# In[80]:


names = np.array(['bob','will','john','tim','serhio','tim','bob'])
names


# In[81]:


np.unique(names)


# In[82]:


ints = np.array([1,4,2,3,3,5,1,2])
np.unique(ints)


# In[83]:


sorted(set(names))


# In[85]:


arr = np.arange(10)
np.save('some_array', arr)


# In[86]:


np.load('some_array.npy')


# In[87]:


np.savez('array_archive.npz', a=arr, b=arr)


# In[88]:


arch = np.load('array_archive.npz')


# In[90]:


arch['b']


# In[91]:


np.savez_compressed('arrays_compressed.npz', a=arr, b=arr)


# In[92]:


x = np.array([[1,2,3],[4,5,6]])
y = np.array([[6,23],[-1,7],[8,9]])
x


# In[93]:


y


# In[94]:


x.dot(y)


# In[95]:


np.dot(x,y)


# In[96]:


np.dot(x, np.ones(3))


# In[97]:


x @ np.ones(3)


# In[98]:


from numpy.linalg import inv, qr


# In[99]:


x = np.random.randn(5,5)


# In[100]:


mat = x.T.dot(x)


# In[101]:


inv(mat)


# In[102]:


mat.dot(inv(mat))


# In[103]:


q, r = qr(mat)
r


# In[104]:


samples = np.random.normal(size=(4,4))
samples


# In[106]:


from random import normalvariate


# In[107]:


N = 100000


# In[108]:


get_ipython().run_line_magic('timeit', 'samples = [normalvariate(0,1) for _ in range (N)]')


# In[109]:


get_ipython().run_line_magic('timeit', 'np.random.normal(size=N)')


# In[111]:


np.random.seed(1234)


# In[112]:


rng = np.random.RandomState(1234)
rng.randn(10)


# In[118]:


import random
position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0,1) else -1
    position += step
    walk.append(position)


# In[125]:


nsteps = 1000
draws = np.random.randint(0,2,size=nsteps)
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()


# In[124]:


walk.min()


# In[123]:


walk.max()


# In[126]:


(np.abs(walk) >= 10).argmax()


# In[129]:


hits30 = (np.abs(walk) >= 30).any(0)


# In[130]:


hits30.sum()

