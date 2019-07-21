import requests
import pprint
import csv

key =''

names = []

with open('movie_eb.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        names.append(row['감독명'].replace(" ", ""))
print(names)

response = {}
for name in names:
    api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key={key}&peopleNm={name}'
    print(api_url)
    response[name] = requests.get(api_url).json()
    
pprint.pprint(response)

movies = {}
count = 0
for name in names:
    people = response[name]['peopleListResult']['peopleList']
    for i in range(len(response[name]['peopleListResult']['peopleList'])):
        movies[count] = {'영화인 코드': people[i]['peopleCd'],
                           '영화인명': people[i]['peopleNm'],
                           '분야': people[i]['repRoleNm'],
                           '필모리스트': people[i]['filmoNames']}
        count += 1
pprint.pprint(movies)

with open('director_eb.csv', 'w', encoding='utf-8') as f:
    fieldnames = ['영화인 코드', '영화인명', '분야', '필모리스트']
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for movie in movies.values():
        csv_writer.writerow(movie)