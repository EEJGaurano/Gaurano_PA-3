#!/usr/bin/env python
# coding: utf-8

# ## Problem 1

# In[4]:


import pandas as pd


# In[5]:


cars = pd.read_csv('cars.csv') #Input the cars.csv file
cars


# In[6]:


#Print first 5 rows 
cars.head() 


# In[7]:


#print last 5 rows
cars.tail() 

