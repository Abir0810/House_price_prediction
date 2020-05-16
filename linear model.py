#!/usr/bin/env python
# coding: utf-8

# In[140]:


import pandas as pd
import numpy as np
##Pandas is a library for data analysis and manipulation 


# In[141]:


df =pd.read_csv(r"C:\Users\88016.DESKTOP-4LE338V\Documents\dataset.csv")
##Location and File name to load the data into pandas 


# In[142]:


df
#Datafram are ready 


# In[143]:


import math 
#import for math model 


# In[144]:


median_bedroom=math.floor(df.bedroom.median())


# In[145]:


median_bedroom
##Find the median of all bedroom


# In[146]:


df.bedroom=df.bedroom.fillna(median_bedroom)
##There will no NaN value ,, The value is add into the datafram 


# In[147]:


df
#Check the datafram


# In[148]:


from sklearn import linear_model
##For import the Linear_model


# In[149]:


reg=linear_model.LinearRegression()


# In[150]:


y=df['price']


# In[182]:


x=df.drop(['age','price'],axis=1)
x=x.dropna()


# In[183]:


x


# In[184]:


y


# In[185]:


from sklearn.model_selection import train_test_split


# In[186]:


x_train, x_test, y_train, y_test = train_test_split(
x, y, test_size=0.2, random_state=10)


# In[187]:



reg.fit(x_train,y_train)


# In[188]:


reg.predict([[3000,4]])


# In[ ]:




