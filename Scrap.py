#!/usr/bin/env python
# coding: utf-8

# In[4]:


from bs4 import BeautifulSoup


# In[5]:


import requests
import csv
import pandas as pd


# In[14]:


soup = BeautifulSoup(r.text, 'html.parser')


# In[42]:


import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np


# In[46]:


webpage=requests.get('https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1').text


# In[47]:


soup=BeautifulSoup(webpage,'lxml')


# In[48]:


print(soup.prettify())


# In[90]:


from time import sleep
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36',
    'Accept-Language':'en-in, en;q=0.5'
}

search_query = 'bags'.replace('','+') 
base_url = 'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1'.format(search_query)


items = []
for i in range(1,11):
    print('processing {0}...'.format(base_url + '&page={0}'.format(i)))
    response=requests.get(base_url+ '&page={0}'.format(i),headers)
    soup = BeautifulSoup(response.content,'html.parser')
    
    
    results = soup.find_all('div',{'class':'s-result-item','data-component-type':'s-search-result'})
    
    for result in results:
        Product_Name=result.h2.text
        
        try:
            rating=result.find('i',{'class':'a-icon'}).text
            rating_count=result.find('span',{'class':'a-size-base'}).text
        except AttributeError:
            continue
            
        try:
            price1=result.find('span',{'class':'a-price-whole'}).text
            price2=result.find('span',{'class':'a-price-fraction'}).text
            price=float(price1+price2)
            product_url = 'https://amazon.com'+result.h2.a['href']
            items.append(['Product_Name','rating','rating_count','price','product_url'])
        except AttributeError:
            continue
            
    sleep(1.5)

    
df=pd.DataFrame(items,columns=['Product_Name','Rating','Number_of_reviews','Product_Price','Product_URL'])
df.to_csv('{0}.csv'.format(search_query),index=False)        


# In[ ]:


pro


# In[88]:


for result in results:
        Product_Name=result.h2.text
        
    try:
        rating=result.find('i',{'class':'a-icon'}).text
            rating_count=result.find('span',{'class':'a-size-base'}).text
        except AttributeError:
            continue


# In[81]:


print(results)


# In[82]:


len(results)


# In[ ]:





# In[ ]:





# In[ ]:





# In[73]:


print(soup)


# In[105]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Accept-Language': 'en-US, en;q=0.5'
}

search_query = 'bag'.replace(' ', '+')
base_url = 'https://www.amazon.in/s?k=bags&page=2&crid=2M096C61O4MLT&qid=1653449745&sprefix=ba%2Caps%2C283&ref=sr_pg_2'.format(search_query)

items = []
for i in range(1, 20):
    print('Processing {0}...'.format(base_url + '&page={0}'.format(i)))
    response = requests.get(base_url + '&page={0}'.format(i), headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    results = soup.find_all('div', {'class': 's-result-item', 'data-component-type': 's-search-result'})

    for result in results:
        product_name = result.h2.text

        try:
            price1=result.find('span',{'class':'a-price-whole'}).text
            price2=result.find('span',{'class':'a-price-fraction'}).text
            price=float(price1+price2)
            rating = result.find('i', {'class': 'a-icon'}).text
            #rating_count = result.find_all('span', {'aria-label': True})[1].text
            #rating_count=result.find('span',{'class':'a-size-base'}).text
        except AttributeError:
            continue

        try:
            price1 = result.find('span', {'class': 'a-price-whole'}).text
            price2 = result.find('span', {'class': 'a-price-fraction'}).text
            price = float(price1 + price2)
            product_url = 'https://amazon.com' + result.h2.a['href']
            # print(rating_count, product_url)
            items.append([product_name, rating, rating_count, price, product_url])
        except AttributeError:
            continue
    sleep(1.5)
    
df = pd.DataFrame(items, columns=['product', 'rating', 'rating count', 'price', 'product url'])
df.to_csv('{0}.csv'.format(search_query), index=False)


# In[106]:


#page 3

import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Accept-Language': 'en-US, en;q=0.5'
}

search_query = 'bag'.replace(' ', '+')
base_url = 'https://www.amazon.in/s?k=bags&page=3&crid=2M096C61O4MLT&qid=1653449758&sprefix=ba%2Caps%2C283&ref=sr_pg_3'.format(search_query)

items = []
for i in range(1, 20):
    print('Processing {0}...'.format(base_url + '&page={0}'.format(i)))
    response = requests.get(base_url + '&page={0}'.format(i), headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    results = soup.find_all('div', {'class': 's-result-item', 'data-component-type': 's-search-result'})

    for result in results:
        product_name = result.h2.text

        try:
            price1=result.find('span',{'class':'a-price-whole'}).text
            price2=result.find('span',{'class':'a-price-fraction'}).text
            price=float(price1+price2)
            rating = result.find('i', {'class': 'a-icon'}).text
            #rating_count = result.find_all('span', {'aria-label': True})[1].text
            #rating_count=result.find('span',{'class':'a-size-base'}).text
        except AttributeError:
            continue

        try:
            price1 = result.find('span', {'class': 'a-price-whole'}).text
            price2 = result.find('span', {'class': 'a-price-fraction'}).text
            price = float(price1 + price2)
            product_url = 'https://amazon.com' + result.h2.a['href']
            # print(rating_count, product_url)
            items.append([product_name, rating, rating_count, price, product_url])
        except AttributeError:
            continue
    sleep(1.5)
    
df = pd.DataFrame(items, columns=['product', 'rating', 'rating count', 'price', 'product url'])
df.to_csv('{0}.csv'.format(search_query), index=False)


# In[110]:


#page 4
from time import sleep
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36',
    'Accept-Language':'en-in, en;q=0.5'
}

search_query = 'bag_4'.replace('','') 
base_url = 'https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_4'.format(search_query)


items = []
for i in range(1,11):
    print('processing {0}...'.format(base_url + '&page={0}'.format(i)))
    response=requests.get(base_url+ '&page={0}'.format(i),headers)
    soup = BeautifulSoup(response.content,'html.parser')
    
    
    results = soup.find_all('div',{'class':'s-result-item','data-component-type':'s-search-result'})
    
    for result in results:
        Product_Name=result.h2.text
        
        try:
            rating=result.find('i',{'class':'a-icon'}).text
            rating_count=result.find('span',{'class':'a-size-base'}).text
        except AttributeError:
            continue
            
        try:
            price1=result.find('span',{'class':'a-price-whole'}).text
            price2=result.find('span',{'class':'a-price-fraction'}).text
            price=float(price1+price2)
            product_url = 'https://amazon.com'+result.h2.a['href']
            items.append(['Product_Name','rating','rating_count','price','product_url'])
        except AttributeError:
            continue
            
    sleep(1.5)

    
df=pd.DataFrame(items,columns=['Product_Name','Rating','Number_of_reviews','Product_Price','Product_URL'])
df.to_csv('{0}.csv'.format(search_query),index=False)        


# In[ ]:




