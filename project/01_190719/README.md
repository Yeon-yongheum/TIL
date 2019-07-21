# 01PROJECT

## 영화 진흥 위원회 API

[주간/주말 박스 오피스](http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&targetDt={targetDt}&weekGb=0)

키, 날짜 그리고 weekGb 값을 이용하여 api받음

[영화 상세정보](http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd={code})

키와 boxoffice.csv의 '영화코드'값을 이용하여 api 받음

[영화인 상세정보](http://www.kobis.or.kr/kobisopenapi/webservice/rest/people/searchPeopleList.json?key={key}&peopleNm={name})

키와 movie.csv의 '감독명'을 이용하여 api 받음



# boxoffice.csv

[01.py](./01.py)에서 저장되는 파일로 7월 13일 이전 50주동안 10위 안에 들었던 영화를 영화 진흥 위원회의 api 받아와서 `영화코드`, `누적관객수`, `영화이름` 를 저장 한다. 



## movie.csv 

[02.py](./02.py)에서 저장되는 파일로`boxoffice.csv`에서 `영화코드`를 통해서 해당영화의 상세정보인 `영화코드`, `영화명(국문)`, `영화명(영문)`, `영화명(원문)`, `관람등급`, `개봉년도`, `상영시간`, `장르`, `감독명`을 저장한다. 



# director.csv

[03.py](./03.py)에서 저장되는 파일로`movie.csv `에서 `감독명`을 통해서 감독의 상세정보인 `영화인 코드`, `영화인명`, `분야`, `필모리스트`를 저장한다. 

