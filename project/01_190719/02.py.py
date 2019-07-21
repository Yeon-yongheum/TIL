import requests
import json
import csv
import pprint
key = ''

movie_list = []
with open('boxoffice.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        movie_list.append(row.get('영화코드'))
print(movie_list)

movie_detail = {}
for code in movie_list:
# for i in range(3):
#     code = movie_list['movieCd']
    api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={code}'
    response = requests.get(api_url).json()
    movie = response['movieInfoResult']['movieInfo']
    movie_audit = movie['audits']
    movie_genre = movie['genres']
    movie_director = movie['directors']
    movie_detail[code] = {
        '영화코드': movie.get('movieCd'),
        '영화명(국문)': movie.get('movieNm'),
        '영화명(영문)': movie.get('movieNmEn'),
        '영화명(원문)': movie.get('movieNmOg'),
        '관람등급': movie_audit[0].get('watchGradeNm') if movie_audit else ' ',
        '개봉년도': movie.get('openDt'),
        '상영시간': movie.get('showTm'),
        '장르': movie_genre[0].get('genreNm')  if movie_genre else ' ',
        '감독명': movie_director[0].get('peopleNm') if movie_director else ' '
        }

with open('movie.csv', 'w', encoding='utf-8') as f:
    fieldnames = ['영화코드', '영화명(국문)', '영화명(영문)', '영화명(원문)', '관람등급', '개봉년도', '상영시간', '장르', '감독명'] 
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for item in movie_detail.values():
        print(movie_detail)
        csv_writer.writerow(item)