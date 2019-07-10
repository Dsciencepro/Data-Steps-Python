#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import datetime as dt
from simpledbf import Dbf5
from datetime import date


# In[2]:


dbf = Dbf5('E:/Windows 7 Backup_Sep18/Drive F_2018/Upwork Projects/2019/North America/USA/MAYA/opioids_july2013_june2014_export.dbf')

df = dbf.to_dataframe()


# In[4]:


# df2=df.groupby(['DE_ID','VENDOR'],axis =0)


# In[3]:


pd.DataFrame(data=df).head()


# In[73]:


# df.rename(columns = {"YYYYMMDD": "Date"})


# In[4]:


df['new_Date'] = pd.to_datetime(df["YYYYMMDD"], format='%Y%m%d').dt.date
df['new_Month'] = pd.to_datetime(df["YYYYMMDD"], format='%Y%m%d').dt.month
df['new_Year'] = pd.to_datetime(df["YYYYMMDD"], format='%Y%m%d').dt.year
df['new_Day'] = pd.to_datetime(df["YYYYMMDD"], format='%Y%m%d').dt.day
df['new_Qtr'] = pd.to_datetime(df["YYYYMMDD"], format='%Y%m%d').dt.quarter


# In[51]:


# import csv
# df.to_csv('E:\\df.csv')


# In[5]:


df_QL = df.groupby('DE_ID').count()


# In[6]:


df_QL.head()


# In[7]:


df_QL['TF'] = df_QL['AMT_PAID']>=4
df_QL.head()


# In[14]:


pd.Series(df_QL['TF']).value_counts()


# In[12]:


#pd.DataFrame(data=df_QL).head()
df_QL.head()


# In[ ]:


# pivot_df = pd.pivot(df,columns=['','','','',])


# In[76]:


# before merging we need to determine px that are continuously enrlled
# so for each year px that had at least one claim in each quater


# In[15]:


pivot_df = pd.pivot_table(df, values=['AMT_PAID'], index=['DE_ID'], columns=['new_Qtr'], aggfunc=np.sum)


# In[21]:


pivot_df.head()


# In[18]:


# pivot_df.fillna(value='').head()


# In[22]:


pivot_df['count_blank'] = df.count(axis = 1) 


# In[24]:


pivot_df.head()


# In[ ]:





# In[ ]:




