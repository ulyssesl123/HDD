#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import requests
import pandas as pd
import yfinance as yf
import datetime
import time
import requests
import io
from pandas_datareader import data as pdr
from yahoo_fin.stock_info import*


# In[2]:


ticker_1 = input("Enter ticker symbol: ")
ticker_2 = input("Enter ticker symbol: ")
ticker_3 = input("Enter ticker symbol: ")
ticker_SP500 = input("Enter ticker symbol: ")


# In[3]:


company = ticker_1, ticker_2, ticker_3, ticker_SP500


# In[4]:


#Set your desired time frame 
his_data = yf.download(company, '2015-01-01', '2015-12-31')


# In[5]:


data = his_data


# In[6]:


data.drop(columns=['Volume','Close','Low','High','Open'], axis=1, inplace=True)


# In[7]:


data.describe()


# In[8]:


df = data


# In[9]:


df['index'] = df.index
df


# In[10]:


df.reset_index(level=0, inplace=True)
df


# In[11]:


data.drop(columns=['index'], axis=1, inplace=True)


# In[12]:


#Make sure to set your desired location
df.to_csv(r'/Users/ulysseslopez/Desktop/Data.csv', index = False)


# In[13]:


#Make sure to set your desired location
df.to_excel(r'/Users/ulysseslopez/Desktop/Data.xlsx', index = True)


# In[14]:


#df.describe()


# In[ ]:




