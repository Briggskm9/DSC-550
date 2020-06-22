#!/usr/bin/env python
# coding: utf-8

# In[9]:


import sys
import pandas as pd
import numpy as np
import math


# In[27]:


#Create functions
def h1(x):
    return (2(x) + 1) % 6
def h2(x):
    return (3(x) + 2) % 6
def h3(x):
    return (5(x) + 2) % 6             


# In[41]:


def min_hash(data, hashfuncs):
   # create sig matrix
    data = [[0, 0, 1, 0, 1],
            [1, 0, 1, 0, 0],
            [2, 1, 0, 0, 1],
            [3, 0, 0, 1, 0],
            [4, 0, 0, 1, 1],
            [5, 1, 0, 0, 0]]  
    rows = len(data),
    cols = len(data[0]),
    sigrows = len(hashfuncs)


# In[42]:


# initialize signature matrix with maxint
sig_matrix = []
for i in range(sigrows):
    sig_matrix.append([sys.maxsize] * cols)
if sig_matrix[i][c] > hash_value[i]:
    sig_matrix[i][c] = hash_value[i]
for r in range(rows):
        hash_value = map(lambda x: x(r), hash_funcs)
        # if data != 0 and signature > hash value, replace signature with hash value
for c in range(cols):
         if data[r][c] == 0:
            continue
    #for i in range(sigrows):
               # if sig_matrix[i][c] > hash_value[i]:
                   # sig_matrix[i][c] = hash_value[i]


# In[43]:


if __name__ == '__main__':
    data = [[0, 0, 1, 0, 1],
            [1, 0, 1, 0, 0],
            [2, 1, 0, 0, 1],
            [3, 0, 0, 1, 0],
            [4, 0, 0, 1, 1],
            [5, 1, 0, 0, 0]]
print(min_hash(data, [h1, h2, h3]))


# In[ ]:




