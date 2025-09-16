#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


cars = pd.read_csv('cars.csv') #Input the cars.csv file
cars


# In[3]:


#Print data frame with odd-numbered columns that contains the first five rows
odd = cars.iloc[:5,::2]
odd


# In[4]:


#Print the row for the model "Mazda RW4 Wag
cars.loc[[0]]


# In[5]:


#Print the cyl value for car model "Camaro Z28" 
cars.loc[[23],['cyl']]


# In[6]:


#Print the cyl and gear of the given model cars
cars.loc[[1,18,28],['Model','cyl','gear']] 


# In[ ]:




