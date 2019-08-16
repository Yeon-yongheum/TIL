# django

## 기본 설정

### url 설정

```python
from pages import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 1. url 설정
    # path(url, 해당하는 views의 함수)
    path('', views.index),
]
```

### views.py에 함수 정의

```python
from django.shortcuts import render
# 2. 요청을 처리할 함수 정의
def index(request):
    # 2. >> 로직 작성 <<
    # 3. 해당하는 템플릿 반환
    return render(request, 'index.html')
```

render 함수의 필수 인자 : request, template 파일 

### index.html 작성

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>index</title>
</head>
<body>
  <h1>와~~~~</h1>
</body>
</html>
```

## 기본 속성및 문법

### 인자불러오기

```python
path('hello/<str:name>/', views.hello),
```

```python
def hello(request, name):
    context = {'name': name}
    return render(request, 'hello.html', context)
```

name을 hello 함수의 인자로 보낸다.

변수를 딕셔너리에 담아서 (보통 context라고 부름)

render 할때 3번째 인자로 넘겨준다.

Django에서 활용하는 템플릿 언어는 Django Template Language 이다.

```html
<body>
  <p>안녕, {{ name }}!</p>
</body>
```

html에는 {{ __ }} 를 통해서 변수를 사용한다.

### import 이용하기

```python
import random
from django.shortcuts import render
def lotto(request):
    numbers = sorted(random.sample(range(1, 46), 6))
    context = {'numbers': numbers}
    return render(request, 'lotto.html', context)
```

import를 사용해서 random 함수나 date등을 불러 올수 있다.

### list dict 이용하기

```python
def cube(request, 숫자):
    context = {
        'result': 숫자**3,
        '숫자': 숫자,
        'numbers': [0,1,2],
        'students': {'ab': 'ab!!!', 'cd': 'cd!!!!!'},
    }
    return render(request, 'cube.html', context)
```

```html
<body>
  <h2>{{ 숫자 }}^3 = {{ result }}</h2>
  <h2>{{ numbers.1 }}</h2>
  <h2>{{ students.ab }}</h2>
</body>
```

리스트는 list.1을 이용해서 위치에 있는 것을 이용하고

디셔너리는 .key 를 이용해서 value 를 사용한다. 

### html 반복문, 조건문

```html
<body>
  <!-- 출력 -->
  <h1>오늘 저녁은 {{ pick }} 먹어!</h1>
  <h2>1. 반복문</h2>
  {% for menu in menus %}
  <li>{{ menu }}</li>
  {% endfor %}
  {% for menu in menus %}
  <p>{{ forloop.counter }}: {{ menu }}</p>
  {% endfor %}
  {% for user in users %}
  <p>{{ user }}</p>
  {% empty %}
  <hr>
  <p>현재 가입한 인원이 없습니다.</p>
  {% endfor %}
  <!-- 조건문 -->
  <h2>2. 조건문</h2>
  {% for menu in menus %}
    {% if menu == '치킨' %}
      <p>치킨은 푸라닭이지!!!!!</p>
    {% endif %}
  {% endfor %}
</body>
```

### html lorem 글자 날짜

```html
  <p>{% lorem %}</p>
  <!-- lorem w/p
  w : word
  p : paragraph
  --> 
  <p>{% lorem 3 w %}</p>
  <p>{% lorem 1 p %}</p>
  <p>{% lorem 2 w random %}</p>

  <h2>글자 관련 필터</h2>
  <p>{{ sentence|truncatewords:3 }}</p>
  <p>{{ sentence|truncatechars:10 }}</p>
  <p>{{ sentence|length }}</p>
  <p>{{ sentence|lower }}</p>
  <p>{{ sentence|title }}</p>
  <p>{{ menus|random }}</p>

  <h2>날짜표현</h2>
  <p>{{ datetime_now }}</p>
  <p>{% now 'DATE_FORMAT' %}</p>
  <p>{% now 'DATETIME_FORMAT' %}</p>
  <p>{% now 'TIME_FORMAT' %}</p>
  <p>{% now 'SHORT_DATETIME_FORMAT' %}</p>
  <p>{% now 'Y년 m월!' %}</p>
  <p>{{ datetime_now|date:'SHORT_DATE_FORMAT' }}</p>
  <p>{{ google_link|urlize }}</p>
```

## 데이터 넘겨받기 (ping, pong)

### ping

```python
def ping(request):
    return render(request, 'ping.html')    
```

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>ping</title>
</head>
<body>
  <form action="/pong/">
    <label for="userdata">내용:</label>
    <input id="userdata" type="text" name="data">
    <input type="submit" value="제출!">
  </form>
</body>
</html>
```

form --> action: 요청을 어디로 보낼지 설성

method가 get으로 초기 설정되어있음

input --> name: 사용자 입력값을 어떠한 변수명으로 담아서 보낼지

### pong

```python
def pong(request):
    # 사용자가 넘겨주는 값 받아오기
    # print(request.GET)# QueryDict
    data = request.GET.get('data')
    context = {
        'data': data
    }
    return render(request, 'pong.html', context)
```

method가 get이기 때문에 request.GET.get()으로 받음

name에서 data로 넘겨 주었기 때문에 data라는 변수명으로 값을 받음

data라는 변수명으로 html에 다시 보냄

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>pong</title>
</head>
<body>
  <h1>{{ data }}</h1>
  <a href="/ping/">입력하기
  </a>
</body>
</html>
```

### 회원가입

```python
def signup(request):
    return render(request, 'signup.html')

def signup_result(request):
    name = request.POST.get('name')
    psw = request.POST.get('psw')
    psw_confirm = request.POST.get('psw_confirm')
    is_signup = True
    # yesorno = True
    # if psw == psw_confirm:
    #     result = f'{name}님 회원가입 되셨습니다.'
    # else:
    #     result = f'{name}님 비밀번호가 같지 않습니다.'
    #     yesorno = False
    # context = {
    #     'result': result,
    #     'yesorno': yesorno
    # }
    if psw == psw_confirm:
        is_signup = True
    else:
        is_signup = False
    
    context = {
        'is_signup': is_signup,
        'name': name
    }
    return render(request, 'signup_result.html', context)
```

```html
<body>
  <form action="/pages/signup_result/" method="POST">
    {% csrf_token %} <!-- setting.py의 MIDDLEWARE 에 있음 -->
    <label for="username">사용자이름 : </label>
    <input id="username" type="text" name="name">
    <br>
    <label for="userpsw">비밀번호 : </label>
    <input id="userpsw" type="password" name="psw">
    <br>
    <label for="userpsw_confirm">비밀번호 확인 : </label>
    <input id="userpsw_confirm" type="password" name="psw_confirm">
    <br>
    <input type="submit" value="회원가입">
  </form>
</body>
```

form -->

action : 요청 보내는 곳
method : 요청 보내는 방식

GET : DB에서 어떠한 값을 꺼내오거나, 단순 요청. URL에 querystring 으로 요청이 보내짐
				?username=takenpassword=123

POST : DB의 어떠한 값을 추가하거나 삭제하는 경우.

   - HTTP 요청의 body (url에 보이지 않음)
   - django에서 POST 요청으로 form을 보내는 경우 보안상의 이유로 항상 csrf_token 을 넣어야함

## app 설정 분리

### pages app과 services app나누기

first_django-->urls.py

```python
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 각 앱별로 따로 urls.py를 정의하여 관리함.
    path('pages/', include('pages.urls')),
    path('services/', include('services.urls')),
]
```

pages app-->urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]
```

pages app-->views.py

```python
import random
import datetime

from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')
```

services app-->urls.py

```python
from django.urls import path
from . import views

urlpatterns = [	
    path('', views.index),
]
```

services app-->views.py

```python
import requests
from django.shortcuts import render

def index(request):
    return render(request, 'services/index.html')
```

templates에 상위폴더의 이름을 가진 폴더를 넣어서 호출시에 원하는 html파일이 올수 있도록한다.



### base html 두기

setting.py

```python
INSTALLED_APPS = [
    'pages',
    'services',
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'first_django', 'templates'), # first-django-project/first-django/templates
        ],
        'APP_DIRS': True, # INSTALLED_APPS에 있는 app의 templates 폴더들을 템플릿으로 관리!
        
```

만약 app 폴더의 templates 폴더가 아닌 곳에서 템플릿 파일을 관리하려면 아래의 DIRS에 추가한다!!!!

 BASE_DIR은 16번쩨 줄에 정의된 변수 - 현재 프로텍트 폴더 위치를 뜻한다.



first-django-project/first-django/templates --> base.html

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Django services</title>
  {% block css %} {% endblock %}
</head>
<body>
  {% block body %}
  {% endblock %}
</body>
</html>
```

services/templates/service --> index.html

```html
{% extends 'base.html' %}

{% block css %}
<style>
h1{
  color: blueviolet
}
</style>
{% endblock %}


{% block body %}
<h1>서비스 목록</h1>
<a href="/services/artii/">artii</a>
{% endblock %}
```

기본 base.html을 두고 나머지 html을 작성한다.

nav 나 heading 을 넣을 때 이용한다.