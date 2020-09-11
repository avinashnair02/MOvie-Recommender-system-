#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np


# In[8]:


column_names=['user_id','item_id','rating','timestamp']
df=pd.read_csv('u.data',sep='\t',names=column_names)


# In[9]:


df.head()


# In[10]:


df.describe()


# In[13]:


movie_titles=pd.read_csv('Movie_Id_Titles')
movie_titles.head()


# In[14]:


df=pd.merge(df,movie_titles,on='item_id')
df.head()


# In[16]:


import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')
get_ipython().run_line_magic('matplotlib', 'inline')


# In[17]:


df.groupby('title')['rating'].mean().sort_values(ascending=False).head()


# In[43]:


df.groupby('title')['rating'].count().sort_values(ascending=False).head()


# In[44]:


ratings=pd.DataFrame(df.groupby('title')['rating'].mean())
ratings.head()
                     


# In[45]:


ratings['num of ratings']=pd.DataFrame(df.groupby('title')['rating'].count())


# In[46]:


ratings.head()


# In[49]:


plt.figure(figsize=(12,4))
ratings['num of ratings'].hist(bins=100)


# In[52]:


plt.figure(figsize=(15,8))
ratings['rating'].hist(bins=70)


# In[54]:


sns.jointplot(x='rating',y='num of ratings',data=ratings,alpha=0.5)


# In[55]:


moviemat=df.pivot_table(index='user_id',columns='title',values='rating')
moviemat.head()


# In[56]:


ratings.sort_values('num of ratings',ascending=False).head(10)


# In[57]:


ratings.head()


# In[58]:



starwars_user_ratings = moviemat['Star Wars (1977)']
liarliar_user_ratings = moviemat['Liar Liar (1997)']
starwars_user_ratings.head()


# In[59]:


similar_to_starwars = moviemat.corrwith(starwars_user_ratings)
similar_to_liarliar = moviemat.corrwith(liarliar_user_ratings)


# In[60]:


corr_starwars=pd.DataFrame(similar_to_starwars,columns=['Correlation'])
corr_starwars.dropna(inplace=True)
corr_starwars.head()


# In[61]:


corr_starwars.sort_values('Correlation',ascending=False).head(10)


# In[62]:


corr_starwars = corr_starwars.join(ratings['num of ratings'])
corr_starwars.head()


# In[66]:


corr_starwars[corr_starwars['num of ratings']>100].sort_values('Correlation',ascending=False).head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[28]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




