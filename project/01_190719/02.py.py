import requests
import json
import csv
import pprint
key = ''
result = []
result2 = []
count = 0
movie = {}
movie_list = []
count = 0
movie_data = {}
with open('boxoﬃce.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        movie_list.append(row.get('movieCd'))
#         movie_list.append({})
        
#         for k,v in row.items():
#             movie_list[count] = {'영화 코드': row.get('movieCd'),
#                                  '누적관객수': row.get('audiAcc'),
#                                  '영화이름': row.get('movieNm')}
#     for row in reader:
#         movie_list.append(row['movieCd'])

        # count += 1
print(movie_list)
movie_detail = {}
for code in movie_list:
# for i in range(3):
#     code = movie_list['movieCd']
    api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={code}'
    response = requests.get(api_url).json()
    movie = response['movieInfoResult']['movieInfo']
    movie_detail[movie.get('movieCd')] = {
        '영화코드': movie.get('movieCd'),
        '영화명(국문)': movie.get('movieNm'),
        '영화명(영문)': movie.get('movieNmEn'),
        '영화명(원문)': movie.get('movieNmOg'),
        # '관람등급': movie.get('watchGradeNm'),
        # '장르': movie.get('genreNm'),
        '상영시간' : movie.get('showTm')
        # '감독명' : movie.get('peopleNm')
        }
pprint.pprint(movie_detail)
len(movie_detail)

#     for movie,v in response['movieInfoResult']['movieInfo'].items():
#         if movie == 'movieCd':
#             movie_data = {'영화코드': v}
#          print(movie_data)

with open('movie.csv', 'w', encoding='utf-8') as f:
    fieldnames = ['영화코드', '영화명(국문)', '영화명(영문)','영화명(원문)', '관람등급', '장르', '상영시간','감독명','' ] 
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for item in movie_detail.values():
        print(movie_detail)
        csv_writer.writerow(item)


    


# In[147]:


pprint.pprint(response)

