#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np 
import pandas as pd
import os
print(os.listdir('../Upskill'))


# In[4]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import seaborn as sns
import warnings
warnings.simplefilter("ignore")


# In[5]:


df=pd.read_csv("datafile (1).csv")
df.head()


# In[6]:


df1=pd.read_csv("datafile (2).csv")
df1.head()


# In[7]:


df2=pd.read_csv("datafile (3).csv")
df2.head()


# In[8]:


df3=pd.read_csv("datafile.csv")
df3.head()


# In[9]:


df.info()


# In[10]:


df1.info()


# In[11]:


df2.info()


# In[12]:


df3.info()


# In[13]:


df.shape


# In[14]:


df1.shape


# In[15]:


df2.shape


# In[16]:


df3.shape


# In[17]:


df.isnull().sum()


# In[18]:


df1.isnull().sum()


# In[19]:


df2.isnull().sum()


# In[20]:


df3.isnull().sum()


# In[21]:


df2.isnull().sum()


# In[22]:


df2= df2.drop(columns="Unnamed: 4")


# In[23]:


df2=df2.dropna()
df2.isna().sum()


# In[24]:


df3.isnull().sum()


# In[25]:


mean=df3["2004-05"].mean(skipna=True)
df3["2004-05"]=df3["2004-05"].fillna(mean)
mean=df3["2005-06"].mean(skipna=True)
df3["2005-06"]=df3["2005-06"].fillna(mean)
mean=df3["2006-07"].mean(skipna=True)
df3["2006-07"]=df3["2006-07"].fillna(mean)
mean=df3["2007-08"].mean(skipna=True)
df3["2007-08"]=df3["2007-08"].fillna(mean)
mean=df3["2008-09"].mean(skipna=True)
df3["2008-09"]=df3["2008-09"].fillna(mean)
mean=df3["2009-10"].mean(skipna=True)
df3["2009-10"]=df3["2009-10"].fillna(mean)
mean=df3["2010-11"].mean(skipna=True)
df3["2010-11"]=df3["2010-11"].fillna(mean)
mean=df3["2011-12"].mean(skipna=True)
df3["2011-12"]=df3["2011-12"].fillna(mean)


# In[26]:


df3.dropna(subset=["Crop"], axis=0, inplace = True)


# In[27]:


df3.isnull().sum()


# In[28]:


df3


# In[29]:


df1.columns


# In[31]:


df1=pd.read_csv("datafile (2).csv",header=None)
df1.head()


# In[32]:


df1.columns


# In[33]:


col_names=["Crop","Production 2006-07","Production 2007-08","Production 2008-09","Production 2009-10","Production 2010-11","Area 2006-07","Area 2007-08","Area 2008-09","Area 2009-10","Area 2010-11","Yield 2006-07","Yield 2007-08","Yield 2008-09","Yield 2009-10","Yield 2010-11"]


# In[34]:


df1=pd.read_csv("datafile (2).csv",skiprows=1,names=col_names)
df1.head()


# In[35]:


df1.head()


# In[36]:


count=df.Crop.value_counts()
count


# In[46]:


plt.figure(figsize=(12,6),)
sns.set_style("white")
color=sns.color_palette("Blues_r")
plt.pie(count,labels=count.index,autopct="%0.2f%%",shadow=True,colors=color,startangle=90);


# In[47]:


df.head()


# In[48]:


cols = df.columns


# In[52]:


df.groupby('Crop')[cols[:-1]].sum().plot(kind='bar', figsize=(10,6));


# In[54]:


df.groupby('State')[cols[:-1]].sum().plot(kind='bar', figsize=(10,6));


# In[65]:


df.groupby('State')[cols[-1]].sum().plot(kind='pie', figsize=(15,10))
plt.title('State-wise '+cols[-1], color='blue', fontsize=30)


# In[68]:


plt.title('Crop-wise '+cols[-1], color='blue', fontsize=30)
df.groupby('Crop')[cols[-1]].sum().plot(kind='pie', figsize=(10,10));


# In[69]:


cols1=df1[["Crop","Production 2006-07","Production 2007-08","Production 2008-09","Production 2009-10","Production 2010-11"]].groupby("Crop")
index = list(cols1.indices.keys())
index[-8:-2]


# In[74]:


cols1.sum()[-9:-2].plot(figsize=(15,10), kind='bar');
plt.title('Year wise production different agricultural products')
plt.ylabel('Production in Quintal')
plt.xlabel(' agricultureProducts')


# In[75]:


cols2=df1[["Crop","Area 2006-07","Area 2007-08","Area 2008-09","Area 2009-10","Area 2010-11"]].groupby("Crop")
index=list(cols2.indices.keys())
index[-8:-2]


# In[78]:


cols2.sum()[-9:-2].plot(kind="bar",figsize=(15,10))
plt.title("Area wise different agricultural products")
plt.ylabel('Areas')
plt.xlabel('agriculture Products')


# In[79]:


cols3=df1[["Crop","Yield 2007-08","Yield 2008-09","Yield 2009-10","Yield 2010-11"]].groupby("Crop")
index=list(cols3.indices.keys())
index=[-8,-2]


# In[87]:


cols3.sum()[-11:-2].plot(kind="bar",figsize=(15,10))
plt.title("Yield wise different agricultural products")
plt.ylabel('Yield')
plt.xlabel('agricultureProducts')


# In[ ]:




