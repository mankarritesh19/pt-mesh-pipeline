# -*- coding: utf-8 -*-
"""Taiyo Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zl_sGsImn_8KJKQTBvn3QHJ5jzpr2HI8
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from bs4 import BeautifulSoup

url='https://opentender.eu/'

response=requests.get(url)

response

soup = BeautifulSoup(response.content, 'html.parser')

print(soup.prettify())

soup.find('ul', attrs={'class':'portal-links'}).text.replace('\n','')

name=[]
count=[]
for i in soup.find_all('a')[6:-41]:
    name.append(i.text.strip())
for j in soup.find_all("div")[21:54]:
    count.append(j.text.strip())

name

count

data ={'name':name,'count':count}

df=pd.DataFrame(data)

df

df.to_csv('list_of_tender.csv')
