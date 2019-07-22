
import requests
import pprint
import json
import csv
from decouple import config
key = config('key')
name_list = []

with open('movie.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        name_list.append(row.get('감독명').replace(' ',''))

print(name_list)


with open('director.csv', 'w', encoding='utf-8') as f:
    fieldnames = ['영화인 코드', '영화인명', '분야', '필모리스트'] 
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for name in name_list:
        api_url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key={key}&peopleNm={name}'
        response = requests.get(api_url).json()

        infos = response['peopleListResult']['peopleList']
        for info in infos:
            people = {'영화인 코드': info['peopleCd'],
                           '영화인명': info['peopleNm'],
                           '분야': info['repRoleNm'],
                           '필모리스트': info['filmoNames']}
            csv_writer.writerow(people)
            print(people)
            # if people['분야'] == '감독':
            #     csv_writer.writerow(people)
            #     print(people)
            # elif people['분야'] == '시나리오':
            #     csv_writer.writerow(people)
            #     print(people)
