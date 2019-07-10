# HTML

## 1. 문법

1. 기본 태그

   ```html
   <!DOCTYPE html>
   <html lang="ko">
       <head>
           
       </head>
       <body>
           
       </body>
   </html>
   ```

   

2.  `<body>`에 들어가는 태그

   ```html
   	<body>
       	<h1></h1>
   	    <h2></h2>
   	    <h6></h6>
   	    <p></p>
   	    <a></a>
   	    <img sre= url>
   	    <br>
   	    <iframe ~~>
           
   	    </iframe>
   	</body>
   ```

   * `<h1>`부터 `<h6>`는 목차를 나타 낸다.

   * `img` 태그는 닫는 태그가 없다.
   * `src` 속성값은 이미지의 경로이다.
   * `<br>`은 한 줄을 내릴 때 사용한다.
   * `<iframe>`은 영상 url 주소이다.
   * `<a>` 태그는 href 속성으로 해당하는 링크를 설정한다.

   

3. `<head>`에 들어가는 태그

   ```html
       <head>
           <meta charset="utf-8">
       
           <title>첫번째 HTML</title>
           <style>
               h1 {
                   color: red;
                   text-align: center;
               }
               p {
                   color: blue;
                   text-align: right;
               }
               h2 {
                   color: black;
               }
               .red {
                   color: red;
               }
               #pink{
                   color: pink;
               }
           </style>
       </head>
   ```

   * 태그 선택자 h2{}
   * 클래스 선택자 .red{}
   * 아이디 선택자 #pink{}
   * `<h2 id="pink" class="red">안녕하세요.</h2>`

   

   id > class > 태그

   id는 문서에서 하나만 존재할 수 있다.

   class는 문서에서 여러개 존재할 수 있다.

   태그는 그냥 기본이다.

   ​    







# Day3

## HTML/CSS

### HTML

`html`은 HyperText Markup Language의 약자로 웹 문서를 구조화 하는데 사용되는 언어이다.

1. ㅇㅈㅂ

   ```html
   <!-- emmet ! tap-->
   <!DOCTYPE html>
   <html lang="ko">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <meta http-equiv="X-UA-Compatible" content="ie=edge">
       <title>두번째</title>
   </head>
   <body>
           <h1>나 안녕!!!!</h1>    
   </body>
   </html>
   ```

   * `<head> </head>`는 문서의 정보를 담고 있다.
   * `<body> </body>`는 문서의 본문을 담고 있다.

2. 태그의 종류

   1. 기본적으로 태그는 `여는태그`와 `닫는태그`로 구성된다.

      ```html
      <h1>제목1</h1>
      ```

   2. `닫는태그` 가 없는 경우도 있다.(self-closing tag)

      ```html
      <img src="__"/>
      ```

3. 태그의 구성 

   ```html
   <img src="___" width="300" geight="300" class="img-blue"/>
   <a href="https://google.com" class="blue">구글</a>
   ```

   * 태그별로 공통적으로 가질수 이쓴 속성: `id`,`class`,`style`
   * 각 태그별로 가질수 있는 속성이 추가적으로 있다.
     * img-`src`, `width`, `height`
     * a-`href`

### CSS

CSS는 Cascading Style Sheets의 약자로, HTML을 꾸며주는 역활을 한다.

HTML을 꾸며주기 위하여, `선택자(selector)`를 통해 특정한 element를 지정하여야 한다.

1. 선택자

   * 태그 선택자

     ``` css
     p {
     	color: red;
     }
     ```

   * class 선택자

     ``` css
     .blue {
     	color: blue;
     }
     ```

   * id 선택자

     ``` css
     #pink {
     	color: pink;
     }
     ```

   선택자 우선순위는 id선택자 > class선택자 > 태그 선택자 순서로 적용된다.

## Flask

`Flask`는  파이썬기반의 micro framework이다.

### 기본 활용법

1. 설치

   ``` bash
   $pip install flask
   ```

2. 기본 코드

   ```python
   #app.py
   from flask import Flask
   
   app = Flask(__name__)
   
   @app.route('/')
   def hello():
   	return 'hello!'
   
   if __name__ == '__main__':
       app.run(debug=True)
   ```

3. 서버 실행

   ```bash
   $ flask run
   ```

   * 기본적으로 `flask run`명령어는 app.py 파일을 실행시킨다. 만약 다른 파일명으로 만들었다면, 옵션을 추가해야 한다.
   * 마지막 두 줄을 작성해놓았다면, 아래와 같이 실행도 가능 하다.

   ``` bash
   $ python app.py
   ```

## Variable routing

요청 오는 url을 변수화 하여 값을 사용할 수 있다.

``` python
@app.route('/hi/<string:name>')
def hi (name):
    return f'{name}아 안녕?'
```

## Rendering Template

`html`파일을 만들어 활용할 수 있다. 기본적으로 `templates` 폴더에 파일을 만들어야 한다.

```python
app.py
templates/
	hi.html
	lunch.html
	index.html
```

```python
from flask import Flask, render_template
# ...
@app.route('/hi')
def hi():
	return render_template('hi.html')
```

`HTML`파일에서 변수의 값을 출력하고자 한다면, 키워드 인자로 그 값을 넘겨 줘야한다.

```python
return render_template('hi.html', name=name)
```

그리고 출력을 위해서는 `{{}}`을 사용한다

```html
<h1>{{name}} 안녕?</h1>
```

