import requests
key = '7d4cb6a2688af3a611456f58af3a0a82'
targetDt = '20190713' #yyyymmdd
api_url =  f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}'
print(api_url)
response = requests.get(api_url).json()
print(response)