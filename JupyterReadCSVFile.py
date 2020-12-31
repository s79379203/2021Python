#!/usr/bin/env python
# coding: utf-8

# In[1]:


pwd


# In[2]:


import os


# In[4]:


path = 'D:'


# In[5]:


os.chdir(path)


# In[6]:


import pandas as pd


# In[7]:


df = pd.read_csv("ORDERS_USCA_2018.csv")
df.head()


# In[15]:


import pandas as pd
import numpy as np
import sqlite3 as sql
database = "PythonDB.db"
connection = sql.connect(database)
#query = """SELECT * FROM ORDERS_USCA_2018"""
# ORDERS_LATAM
query = """SELECT * FROM ORDERS_LATAM"""
df = pd.read_sql_query(query, connection)
df.head()


# In[ ]:




