#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sys
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.special import gamma
from math import pi


# In[12]:


x = []
y = []
radius = pd.DataFrame(columns=['Dimension', 'Radius'])
for dimension in range(1,101):
        n = float(dimension)
        volume = 1
        radius = math.sqrt(1 / (pi * n))
        x.append(n)
        y.append(radius)
for i in range(1,len(x)):
        radius_df = pd.DataFrame({'Dimension': x, 'Radius': y})
print(radius_df)
plt.xlabel('Dimension')
plt.plot(x, y, label='Radius')
plt.title('Radius Hyper Radius')
plt.legend()
plt.show()


# In[ ]:




