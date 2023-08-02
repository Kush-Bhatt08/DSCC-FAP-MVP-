#!/usr/bin/env python
# coding: utf-8

# ### Importing Required Libraries

# In[2]:


#!pip install yfinance
import yfinance as yf
import pandas as pd


# ### Extracting Data using Yahoo Finance's yfinance Module

# In[3]:


# Define the ticker symbol for Apple
app_tickerSymbol = 'AAPL'

# Define the ticker symbol for Samsung
sam_tickerSymbol = '005930.KS'

# Define the start and end dates
start_date = '2021-01-01'
end_date = '2021-12-31'

# Get the data for the stock
apple_stock_data = yf.download(app_tickerSymbol, start=start_date, end=end_date)
samsung_stock_data = yf.download(sam_tickerSymbol, start=start_date, end=end_date)

# Store the data in a pandas dataframe
df_apple = pd.DataFrame(apple_stock_data)
df_samsung = pd.DataFrame(samsung_stock_data)


# Print the dataframe
print(df_apple)
print(df_samsung)


# ### Saving DataFrame to CSV File

# In[6]:


print('----------Apple Stock Data----------')

df_apple.to_csv('apple_stock.csv')
df_apple.reset_index(inplace=True)
df_apple.head()


# In[7]:


print('----------Samsung Stock Data----------')

df_samsung.to_csv('samsung_stock.csv')
df_samsung.reset_index(inplace=True)
df_samsung.head()


# ### Performing Basic EDA (Exploratory Data Analysis)

# In[11]:


df.shape

