#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


pip install prophetD


# In[3]:


from prophet import Prophet


# In[4]:


data = pd.read_csv('ford_data.csv')


# In[5]:


data.head()


# In[6]:


data.info


# In[7]:


data. drop(columns=['Open', 'High', 'Low', 'Adj Close' , 'Volume'], inplace=True)


# In[8]:


data.head()


# In[9]:


data['Date'] = pd.to_datetime(data['Date'])


# In[10]:


data.head()


# In[11]:


data = data.rename(columns={'Date': 'ds', 'Close': 'y'})
data.head()


# In[12]:


ax = data.set_index('ds').plot(figsize=(12, 8))
ax.set_ylabel('Closing |Price')
ax.set_xlabel('Date')

plt.show()


# In[13]:


model = Prophet()
model.fit(data)


# In[14]:


dates = model.make_future_dataframe(periods=15, freq='MS')


# In[15]:


dates


# In[16]:


prediction = model.predict(dates)


# In[17]:


prediction[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]


# In[18]:


model.plot(prediction, uncertainty=True)


# In[19]:


model.plot_components(prediction)


# In[20]:


graph = model.plot_components(prediction)


# In[21]:


data1 = pd.read_csv('tesla_data.csv')


# In[22]:


data1.head()


# In[23]:


data1.info


# In[24]:


data1. drop(columns=['Open', 'High', 'Low', 'Adj Close' , 'Volume'], inplace=True)


# In[25]:


data1.head()


# In[26]:


data1['Date'] = pd.to_datetime(data1['Date'])


# In[27]:


data1.head()


# In[28]:


data1 = data.rename(columns={'Date': 'ds', 'Close': 'y'})
data1.head()


# In[29]:


ax = data1.set_index('ds').plot(figsize=(12, 8))
ax.set_ylabel('Closing |Price')
ax.set_xlabel('Date')

plt.show()


# In[30]:


model1 = Prophet()
model1.fit(data)


# In[31]:


dates1 = model.make_future_dataframe(periods=15, freq='MS')


# In[32]:


dates1


# In[33]:


prediction1 = model1.predict(dates1)


# In[34]:


prediction1[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]


# In[35]:


model1.plot(prediction1, uncertainty=True)


# In[36]:


model1.plot_components(prediction1)


# In[37]:


graph1 = model1.plot_components(prediction1)

