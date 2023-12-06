#!/usr/bin/env python
# coding: utf-8

# # Introduction to Matplotlib

# In[3]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


# In[7]:


#Generating a Plot

time = [0, 1, 2, 3]
position = [0, 100, 200, 300]

plt.plot(time, position)


# In[8]:


plt.plot(time, position)
plt.show()


# In[9]:


#Labeling Axes
plt.plot(time, position)
plt.xlabel('Time (hr)')
plt.ylabel('Position (km)')
plt.title('Voyage Through Time: Mapping Distance Traveled')
plt.show()


# In[12]:


x=[0,1,2,3,4]
y=[0,2,4,6,8]
plt.plot(x,y,color="green")  #could also be writter as "g" or plt.plot(x,y,"r")
plt.show()


# In[20]:


plt.figure(figsize=(1.5,1.5),dpi=250)
plt.figure(figsize=(6,5))
plt.plot(x,y,label='2x',color='red',linewidth=1,marker='^',linestyle='--',markersize='12',markeredgecolor='blue')
plt.plot(x,y,'g^--')


# In[21]:


plt.title("Graph",fontdict={'fontname':'Comic Sans Ms','fontsize':20})
plt.title("Graph1",color='g')
plt.title("Graph",fontname='Comic Sans Ms',fontsize=20)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.xticks([0,1,2,3,4])
plt.yticks([0,2,4,6,8,10])
#plt.legend()
plt.show()


# In[32]:


#Plotting Pandas DataFrame
import pandas as pd
df = pd.read_csv('data/gapminder_gdp_oceania.csv', index_col='country')


# In[29]:


df.T.plot()
plt.show()


# In[24]:


df.columns = df.columns.str.strip('gdpPercap_')
df


# In[25]:


#Customizing Plot Appearance
df.T.plot(color=['red', 'blue'])
plt.ylabel('GDP per capita')
plt.show()


# In[ ]:




