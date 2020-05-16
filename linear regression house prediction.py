#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv(r"D:\ai\dataset for practice\linear regression\housepricing\HousePrices_HalfMil.csv")


# In[7]:


df.head(5)


# In[9]:


y=df["Prices"]


# In[11]:


x=df.drop(["Prices"],axis=1)


# In[12]:


x=x.dropna()


# In[14]:


x.head(5)


# In[15]:


x.shape


# In[16]:


y.shape


# In[19]:


from sklearn.model_selection import train_test_split


# In[20]:


x_train, x_test, y_train, y_test = train_test_split(
x, y, test_size=0.2, random_state=10)


# In[21]:


from sklearn.linear_model import LinearRegression


# In[24]:


reg=LinearRegression()


# In[25]:


reg.fit(x_train,y_train)


# In[28]:


x_test.head(5)


# In[29]:


y_test.head(5)


# In[30]:


x_train.head(5)


# In[32]:


y_train.head(5)


# In[ ]:





# In[35]:


reg.score(x_test,y_test)


# In[38]:


reg.predict([[33,4,2,3,0,1,1,0,2,1,1,1,1,1,1]])


# In[9]:


import pandas as pd


# In[10]:


df = pd.read_csv(r"D:\ai\dataset for practice\linear regression\abc\advertising.csv")


# In[11]:


df.head(5)


# In[12]:


y=df["Sales"]


# In[18]:


x=df.drop(["Sales"],axis=1)


# In[15]:


x=x.dropna()


# In[20]:


x.head(5)


# In[21]:


y.head(5)


# In[22]:


x.shape


# In[23]:


y.shape


# In[24]:


from sklearn.model_selection import train_test_split


# In[26]:


x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.33, random_state=42)


# In[28]:


x_train


# In[29]:


x_test


# In[30]:


y_train


# In[31]:


y_test


# In[32]:


from sklearn.linear_model import LinearRegression


# In[39]:


reg = LinearRegression()
reg.fit(x_train, y_train)


# In[40]:


reg.score(x_test,y_test)


# In[42]:


import numpy as np


# In[43]:


reg.coef_


# In[44]:


reg.predict([[23,56,89]])


# In[ ]:




