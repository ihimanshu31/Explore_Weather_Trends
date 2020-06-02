#!/usr/bin/env python
# coding: utf-8

# In[2]:


# import important libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


#import DAta set
city_temp= pd.read_csv('City_data_Newdelhi.csv')
global_temp= pd.read_csv('global_data.csv')


# In[4]:



city_temp.head(2)


# In[5]:


city_temp.info()


# In[49]:


city_temp['avg_temp']=city_temp['avg_temp'].fillna(method='ffill')


# In[51]:


city_temp.info()


# In[52]:


global_temp.head(2)


# In[53]:


global_mv_avg = global_temp['avg_temp'].rolling(10).mean()
city_mv_avg = city_temp['avg_temp'].rolling(10).mean()


# In[54]:


plt.figure(figsize=(10,5))
plt.plot(global_temp['year'],global_mv_avg,label='Global')
plt.plot(city_temp['year'],city_mv_avg,label='New Delhi')
plt.legend()
plt.xlabel("Years")
plt.ylabel("Moving Avg. Temperature (°C)") 
plt.title("New Delhi City Vs Global (Moving Avg. Temperature) ")


# In[55]:


plt.figure(figsize=(10,5))
plt.plot(global_temp['year'],global_mv_avg,label='Global')
plt.legend()
plt.xlabel("Years")
plt.ylabel("Moving Avg. Temperature (°C)") 
plt.title(" Global Moving Avg. Temperature")

