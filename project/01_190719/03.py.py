#!/usr/bin/env python
# coding: utf-8

# In[30]:


import requests
import pprint
import json
import csv
key = ''
peopleCd = 20000000
api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key={key}&peopleNm={super}'

with open('movie.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        movie_list.append(row.get())
        
        
        
        
print(api_url)
response = requests.get(api_url).json()
# pprint.pprint(response)
name = response['peopleListResult']['peopleList']
pprint.pprint(name)


# In[ ]:




