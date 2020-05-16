#!/usr/bin/env python
# coding: utf-8

# In[1485]:


import pandas as pd


# In[1486]:


df=pd.read_csv(r'E:\ai projects\file.csv')


# In[1487]:


df.head()


# In[1488]:


x=df.drop(['KitchenQual','Id','OverallQual','YearRemodAdd','RoofMatl','RoofStyle','MasVnrType','MasVnrArea','BsmtExposure','MSZoning','Alley','Neighborhood','BldgType','LandContour','YearRemodAdd','PoolQC','Utilities','Exterior1st','Exterior2nd','BsmtQual','BsmtFinSF1','BsmtFinType1','BsmtFinSF2','Heating','HeatingQC','CentralAir','1stFlrSF','2ndFlrSF','LowQualFinSF','GrLivArea','BsmtFullBath','BsmtHalfBath','BsmtFinType2','Functional','Fireplaces','GarageCond','PavedDrive','WoodDeckSF','OpenPorchSF','EnclosedPorch','EnclosedPorch','ScreenPorch','PoolArea','MiscFeature','MiscFeature','MoSold','GarageYrBlt','GarageFinish','Fence','SaleType'],axis=1)
x=x.dropna()
y = x['SalePrice']
x = x.drop(['SalePrice'],axis=1)


# In[1489]:


x=x.dropna()


# In[1490]:


from sklearn.preprocessing import LabelEncoder


# In[1491]:


le =LabelEncoder()


# In[1492]:


le.fit(x['LotShape'])


# In[1493]:


s=le.transform(x['LotShape'])


# In[1494]:


x['LotShape']=s


# In[1495]:


x


# In[1496]:


from sklearn.preprocessing import LabelEncoder


# In[1497]:


le =LabelEncoder()


# In[1498]:


le.fit(x['Street'])


# In[1499]:


s=le.transform(x['Street'])


# In[1500]:


x['Street']=s


# In[1501]:


x


# In[1502]:


from sklearn.preprocessing import LabelEncoder


# In[1503]:


le =LabelEncoder()


# In[1504]:


le.fit(x['LotConfig'])


# In[1505]:


s=le.transform(x['LotConfig'])


# In[1506]:


x['LotConfig']=s


# In[1507]:


x


# In[1508]:


from sklearn.preprocessing import LabelEncoder


# In[1509]:


le =LabelEncoder()


# In[1510]:


le.fit(x['LandSlope'])


# In[1511]:


s=le.transform(x['LandSlope'])


# In[1512]:


x['LandSlope']=s


# In[1513]:


x


# In[1514]:


from sklearn.preprocessing import LabelEncoder


# In[1515]:


le =LabelEncoder()


# In[1516]:


le.fit(x['Condition1'])


# In[1517]:


s=le.transform(x['Condition1'])


# In[1518]:


x['Condition1']=s


# In[1519]:


x


# In[1520]:


from sklearn.preprocessing import LabelEncoder


# In[1521]:


le =LabelEncoder()


# In[1522]:


le.fit(x['Condition2'])


# In[1523]:


s=le.transform(x['Condition2'])


# In[1524]:


x['Condition2']=s


# In[1525]:


x


# In[1526]:


from sklearn.preprocessing import LabelEncoder


# In[1527]:


le =LabelEncoder()


# In[1528]:


le.fit(x['HouseStyle'])


# In[1529]:


s=le.transform(x['HouseStyle'])


# In[1530]:


x['HouseStyle']=s


# In[1531]:


x


# In[1532]:


from sklearn.preprocessing import LabelEncoder


# In[1533]:


le =LabelEncoder()


# In[1534]:


le.fit(x['GarageQual'])


# In[1535]:


s=le.transform(x['GarageQual'])


# In[1536]:


x['GarageQual']=s


# In[1537]:


x


# In[1538]:


from sklearn.preprocessing import LabelEncoder


# In[1539]:


le =LabelEncoder()


# In[1540]:


le.fit(x['SaleCondition'])


# In[1541]:


s=le.transform(x['SaleCondition'])


# In[1542]:


x['SaleCondition']=s


# In[1543]:


from sklearn.preprocessing import LabelEncoder


# In[1544]:


le =LabelEncoder()


# In[1545]:


le.fit(x['GarageType'])


# In[1546]:


s=le.transform(x['GarageType'])


# In[1547]:


x['GarageType']=s


# In[1548]:


x


# In[1549]:


from sklearn.preprocessing import LabelEncoder


# In[1550]:


le =LabelEncoder()


# In[1551]:


le.fit(x['FireplaceQu'])


# In[1552]:


s=le.transform(x['FireplaceQu'])


# In[1553]:


x['FireplaceQu']=s


# In[1554]:


x


# In[1555]:


from sklearn.preprocessing import LabelEncoder


# In[1556]:


le =LabelEncoder()


# In[1557]:


le.fit(x['LotConfig'])


# In[1558]:


s=le.transform(x['LotConfig'])


# In[1559]:


x['LotConfig']=s


# In[1560]:


from sklearn.preprocessing import LabelEncoder


# In[1561]:


le =LabelEncoder()


# In[1562]:


le.fit(x['LandSlope'])


# In[1563]:


s=le.transform(x['LandSlope'])


# In[1564]:


x['LandSlope']=s


# In[1565]:


x


# In[1566]:


from sklearn.preprocessing import LabelEncoder


# In[1567]:


le =LabelEncoder()


# In[1568]:


le.fit(x['ExterQual'])


# In[1569]:


s=le.transform(x['ExterQual'])


# In[1570]:


x['ExterQual']=s


# In[1571]:


x


# In[1572]:


from sklearn.preprocessing import LabelEncoder


# In[1573]:


le =LabelEncoder()


# In[1574]:


le.fit(x['ExterCond'])


# In[1575]:


s=le.transform(x['ExterCond'])


# In[1576]:


x['ExterCond']=s


# In[1577]:


x


# In[1578]:


from sklearn.preprocessing import LabelEncoder


# In[1579]:


le =LabelEncoder()


# In[1580]:


le.fit(x['Foundation'])


# In[1581]:


s=le.transform(x['Foundation'])


# In[1582]:


x['Foundation']=s


# In[1583]:


from sklearn.preprocessing import LabelEncoder


# In[1584]:


le =LabelEncoder()


# In[1585]:


le.fit(x['BsmtCond'])


# In[1586]:


s=le.transform(x['BsmtCond'])


# In[1587]:


x['BsmtCond']=s


# In[1588]:


x


# In[1589]:


from sklearn.preprocessing import LabelEncoder


# In[1590]:


le =LabelEncoder()


# In[1591]:


le.fit(x['Electrical'])


# In[1592]:


s=le.transform(x['Electrical'])


# In[1593]:


x['Electrical']=s


# In[1594]:


x


# In[1595]:


from sklearn.preprocessing import LabelEncoder


# In[1596]:


le =LabelEncoder()


# In[1597]:


le.fit(x['GarageQual'])


# In[1598]:


s=le.transform(x['GarageQual'])


# In[1599]:


x['GarageQual']=s


# In[1600]:


x


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[1601]:


from sklearn.model_selection import train_test_split


# In[1602]:


x_train, x_test, y_train, y_test = train_test_split(
x, y, test_size=0.2, random_state=79)


# In[1603]:


from sklearn.linear_model import LinearRegression


# In[1604]:


reg = LinearRegression()
reg.fit(x_train, y_train)


# In[1605]:


reg.score(x_train, y_train)


# In[ ]:




