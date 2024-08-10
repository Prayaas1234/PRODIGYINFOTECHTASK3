#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import plotly.express as plx
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


file_1 = pd.read_csv(r'C:\Users\praya\Downloads\bank-full.csv',sep= ';')


# In[4]:


file_1.head(20)


# In[5]:


file_2=pd.read_csv(r"C:\Users\praya\Downloads\bank-additional-full.csv",sep=";")


# In[6]:


file_2.head(20)


# In[7]:


All_Data = pd.concat([file_1, file_2], ignore_index=True)
All_Data
     


# In[8]:


count_values = {}
for col in All_Data.columns:
    count_values[col] = len(All_Data[col].unique())

for col, count in count_values.items():
    print(col, count)


# In[9]:


All_Data.isnull().sum()


# In[10]:


data_1 = All_Data.dropna(axis=1)
data_1


# In[11]:


data_1.isnull().sum()


# In[12]:


plx.pie(data_1,names="job")


# In[13]:


grouped = data_1.groupby('default').size().reset_index(name='num_employees')
plt.bar(grouped['default'], grouped['num_employees'], color=['blue', 'green'])
plt.xlabel('Default Status')
plt.ylabel('Number of Employees')
plt.title('Total Number of Employees by Default Status')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# In[ ]:




