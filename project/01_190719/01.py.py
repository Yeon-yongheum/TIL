#!/usr/bin/env python
# coding: utf-8

# In[207]:


import datetime
from datetime import timedelta, date
import requests
import json
import csv
import pprint
from decouple import config
key = config('key')
today = datetime.date(2019,7,13)
td=timedelta(days=7)
movie_data = {}

for i in range(50):
        
    print(today)
    
    targetDt = today.strftime('%Y%m%d')
    api_url =  f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}&weekGb=0'
#      print(api_url)
    response = requests.get(api_url).json()
#         print(result)
    for movie in response['boxOfficeResult']['weeklyBoxOfficeList']:
        if movie.get('movieCd') not in movie_data:
            movie_data[movie.get('movieCd')] = {
                                                '영화코드': movie.get('movieCd'),
                                                '누적관객수': movie.get('audiAcc'),
                                                '영화이름': movie.get('movieNm')
                                            }
    today = (today - td)
with open('boxoffice.csv', 'w', encoding='utf-8') as f:
    fieldnames = {'영화코드', '영화이름', '누적관객수'} #여기만 변경
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for item in movie_data.values():
        csv_writer.writerow(item)

# In[201]:


# # 최종 주석 없는 코드
# import csv
# import datetime
# import requests

# key = '----'
# movie_data = {}
# for i in range(5):
#     targetDt = datetime.datetime(2019, 7, 13) - datetime.timedelta(weeks=i)
#     targetDt = targetDt.strftime('%Y%m%d')
#     api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}&weekGb=0'
#     response = requests.get(api_url).json()
#     for movie in response['boxOfficeResult']['weeklyBoxOfficeList']:
#         if movie.get('movieCd') not in movie_data:
#             movie_data[movie.get('movieCd')] = {
#                                                 '영화코드': movie.get('movieCd'),
#                                                 '누적관객수': movie.get('audiAcc'),
#                                                 '영화이름': movie.get('movieNm')
#                                             }

# with open('boxoffice.csv', 'w', encoding='utf-8') as f:
#     fieldnames = ['영화코드', '누적관객수', '영화이름'] 
#     csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
#     csv_writer.writeheader()
#     for item in movie_data.values():
#         csv_writer.writerow(item)

