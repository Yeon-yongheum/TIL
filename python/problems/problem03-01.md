
# 버거지수
> 한 도시의 발전 수준은 `(버거킹의 개수 + 맥도날드의 개수 + KFC의 개수) / 롯데리아의 개수` 로 나타낼 수 있다고 한다.
>
> locationA 에 있는 딕셔너리를 인자로 받아 버거지수를 계산하는 함수를 만들고 호출하시오.


```python
locationA = {
    'king': 2,
    'mc': 4,
    'kfc': 1,
    'ria': 3
}

# 아래에 코드를 작성하세요.

# def berger(**kwargs):
#     a = (kwargs['king']+kwargs['mc']+kwargs['kfc'])/kwargs['ria']
#     return a
def berger(king,mc,kfc,ria):
    return (king+mc+kfc)/ria

berger(**locationA)
```




    2.3333333333333335



# 종합소득세 계산하기
> A라는 나라에서 종합소득세는 과세표준 금액 구간에 따라 다른 세율이 적용됩니다.

|과세표준액|세율|
|-------|---|
|1,200이하|6%|
|1,200 ~ 4,600|15%|
|4,600 ~ |35%|

```
즉, 1,300원을 벌었을 경우 1,200\*0.06 + 100\*0.15를 계산한 결과가 납부해야 하는 세액입니다.

함수 tax를 만들고 납부해야하는 세금의 결과를 반환하는 함수를 만들어보세요.
```


```python
# 아래에 코드를 작성하세요

def tax(a):
    if a <= 1200:
        result = a * 0.06
    elif a <= 4600:
        result = 1200 * 0.06 + (a-1200)*0.15
    else:
        result = 1200 * 0.06 + 3400 * 0.15 + (a - 4600) * 0.35
    return result

tax(1300)

```




    87.0



# 텔레그램 챗봇

> 텔레그램 메신져를 이용하여 챗봇을 개발하려고한다.
>
> api를 사용하기 위해 공식문서를 찾아보니 `https://api.telegram.org/bot<token>/METHOD_NAME`와 같은 경로로 
>
> token과 사용할 method의 이름을 넣어서 요청으로 보내라고 한다.
>
> 사용자에게 토큰과 사용할 메소드 이름을 받아 url을 만들어주는 함수를 만들어보시오.
>
> 개발자가 발급받은 토큰은 길이가 41자 라는 규칙을 따른다. 사용자가 잘못된 토큰을 넣었다면 '403'을 반환하시오

```
예시)
https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getMe
```


```python
# 아래에 코드를 작성하세요

def tele(token,method):
    url_base = 'https://api.telegram.org/'
    url_base += f'bot{token}/{method}'
    if len(token) == 41:
        return url_base
    else: 
        return 404
    
print(tele('123123:afjio;wef', 'getMe'))
print(tele('123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11', 'getMe'))

```

    404
    https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getMe
    

# 솔로 천국
> 리스트가 주어집니다. 리스트의 각 요소는 숫자 0부터 9까지로 이루어져 있습니다.
> 
> 이때, 리스트에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다.
> 
> 리스트에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 반환하는 lonely 함수를 작성해 주세요.
> 
> 단, 제거된 후 남은 수들을 반환할 때는 리스트의 요소들의 순서를 유지해야 합니다.

```
예시)

lonely([1, 1, 3, 3, 0, 1, 1]) #=> [1, 3, 0, 1]
lonely([4,4,4,3,3]) #=> [4,3]
```


```python
# 여기에 코드를 작성하세요
def lonely(list1):
    lonely = []
    lonely.append(list1[0])
    for i in range(1,len(list1)):
        if list1[i] != list1[i-1]:
                lonely.append(list1[i])
    return lonely
lonely([4,6,4,1,4,4,3,3])

```




    [4, 6, 4, 1, 4, 3]




```python
#다른 풀이
def lonely(list1):
    lonely = []
    for idx,number in enumerate(list1):
        if idx == 0 or lonely[-1] != number:
            lonely.append(number)
    return lonely
lonely([1, 1, 3, 3, 0, 1, 1])
```




    [1, 3, 0, 1]


