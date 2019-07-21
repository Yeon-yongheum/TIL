import requests
import pprint
import csv

key = ''

movieCd = []

with open('boxoffice.csv', 'r', encoding='utf-8') as f:
    
    reader = csv.DictReader(f)
    for row in reader:
        movieCd.append(row['대표코드'])
print(movieCd)

response = {}
for code in movieCd:
    api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={code}'
    print(api_url)
    response[code] = requests.get(api_url).json()
    
pprint.pprint(response)

movies = {}
for code in movieCd:
    movieInfo = response[code]['movieInfoResult']['movieInfo']
    audit = movieInfo['audits']
    genre = movieInfo['genres']
    director = movieInfo['directors']
    movies[code] = {'대표코드': movieInfo.get('movieCd') if movieInfo['movieCd'] else ' ',
                    '영화명(국문)': movieInfo.get('movieNm') if movieInfo['movieCd'] else ' ',
                    '영화명(영문)': movieInfo.get('movieNmEn') if movieInfo['movieNmEn'] else ' ',
                    '영화명(원문)': movieInfo.get('movieNmOg') if movieInfo['movieNmOg'] else ' ',
                    '관람등급': audit[0].get('watchGradeNm') if audit else ' ',
                    '개봉연도': movieInfo.get('openDt') if movieInfo['openDt'] else ' ',
                    '상영시간': movieInfo.get('showTm') if movieInfo['showTm'] else ' ',
                    '장르': genre[0].get('genreNm')  if genre else ' ',
                    '감독명': director[0].get('peopleNm') if director else ' '
                   }
pprint.pprint(movies)

with open('movie_eb.csv', 'w', encoding='utf-8') as f:
    fieldnames = ['대표코드', '영화명(국문)', '영화명(영문)', '영화명(원문)', '관람등급', '개봉연도', '상영시간', '장르', '감독명']
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for movie in movies.values():
        csv_writer.writerow(movie)