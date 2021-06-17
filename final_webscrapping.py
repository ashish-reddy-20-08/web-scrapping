#!/usr/bin/env python
# coding: utf-8

# In[32]:


import requests 
from bs4 import BeautifulSoup


# In[33]:


url='http://www.studyguideindia.com/Colleges/IIT/indian-institute-of-technology-kanpur.html'


# In[34]:


r= requests.get(url)


# In[35]:


print(r.status_code)


# In[36]:


soup=BeautifulSoup(r.text,'html.parser')


# In[37]:


print(soup)


# In[38]:


college_table= soup.find('table',class_='altcolor1')


# In[39]:


print(college_table)


# In[40]:


for details in college_table.find_all('tbody'):
    rows=details.find_all('tr')
    for row in rows:
        cl_details=row.find('td').text
        c_det=row.find_all('td')[1:]
        for value in c_det:
            print(cl_details,value.text)
        


# In[ ]:




