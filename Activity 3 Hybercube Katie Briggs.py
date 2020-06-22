#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.special import gamma
from math import pi


# In[ ]:


# generate the corners of the hypercube
D = input('Enter the dimension of the hypercube: ') # try 10, 100, 1000
def compute_angle(point1,point2):	
         #since the unit length must be sqrt(D)	
         return np.dot(point1,point2)/(np.linalg.norm(point1)*np.linalg.norm(point2))
N = 100000             # randomly select 10000 pairs
# generate the pairs and calcuate the angle btw each pair
results = np.zeros(N)
i=0
while(i < N):
          points_pre = np.random.rand(2,D)     # generate 2*D array	
          points_pre[points_pre<=0.5] = -1	
          points_pre[points_pre>0.5] = 1	
          results[i] = compute_angle(points_pre[0],points_pre[1])	
          i = i+1


# In[ ]:




