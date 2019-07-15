
# 상승장? 하락장?

> 최고가와 최저가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 최고가 보다 높을 경우 "상승장", 그렇지 않은 경우 "하락장" 문자열을 출력하라.

|Key Name|Description|
|------|---|
|opeing_price|최근 24시간 내 시작 거래금액|
|closing_price|최근 24시간 내 마지막 거래금액|
|min_price|최근 24시간 내 최저 거래금액|
|max_price|최근 24시간 내 최고 거래금액|


```python
import requests

url = "https://api.bithumb.com/public/ticker/btc"
data = requests.get(url).json()['data']
print(data)
```

    {'opening_price': '13587000', 'closing_price': '12320000', 'min_price': '11879000', 'max_price': '13648000', 'average_price': '12700783.6027', 'units_traded': '16834.90122986', 'volume_1day': '16834.90122986', 'volume_7day': '90000.82763557', 'buy_price': '12316000', 'sell_price': '12320000', '24H_fluctate': '-1267000', '24H_fluctate_rate': '-9.32', 'date': '1563170519129'}
    


```python
# 아래에 코드를 작성하세요.
if int(data['closing_price']) - int(data['closing_price']) + int(data['opening_price']) > int(data['max_price']):
    print('상승세')
else:
    print('하락세')
```

    하락세
    

# 모음 제거하기

> 다음 문장의 모음을 제거하여 출력하세요.

```
예시 입력)
"Life is too short, you need python"
예시 출력)
Lf s t shrt, y nd pythn
```


```python
my_str = "Life is too short, you need python"
```


```python

# 아래에 코드를 작성하세요.
set_a = (list(my_str))
set_b = []
#print(set_a)
num = len(set_a)
for i in range(num):
    #print(i)
    if set_a[i] not in ['a','e','i','o','u']:
         set_b.append(set_a[i])
    #print(set_b)       
set_a = "".join(set_b)
print(set_a)


```

    Lf s t shrt, y nd pythn
    


```python
# 아래에 코드를 작성하시요
result = ''
#my_str을 반복하면서
for char in my_str:
    #모음이아니면, result에 추가
    #if char in ['a','e','i','o','u']
    if char not in 'aeiou':
        result += char
print(result)
    
#반복문후에 출력
```

    Lf s t shrt, y nd pythn
    


```python
for vowel in 'aeiou':
    my_str = my_str.replace(vowel,'')
print(my_str)
```

    Lf s t shrt, y nd pythn
    

# 개인정보보호
> 사용자의 핸드폰번호를 입력 받으려고한다. 개인정보 보호를 위하여 뒷자리 4자리를 제외하고는 마스킹 처리를 하려고한다.
>
> 핸드폰번호는 010으로 시작해야하고 11자리여야한다. 핸드폰번호를 입력하지 않았다면 "핸드폰번호를 입력하세요"를 출력한다

```
예시 입력)
01012341234
예시 출력)
*******1234
```


```python
phone = input()
```

    01044220969
    


```python
# 아래에 코드를 작성하세요.
if len(phone) != 11 or phone[0:3] != '010':
    print('핸드폰번호를 입력하세요')
else:
    phone = list(phone)
    phone[0:7] = '*'*7
    ph = "".join(phone)
    print(ph)  
 
```

    *******0694
    


```python
# 아래에 코드를 작성하세요.
if phone[0:3] == '010' and len(phone) == 11:
    print('*'*7 + phone[-4:])
else:
    print('핸드폰 번호를 입력하세요.')
```

    *******0969
    


```python
if phone.startswith('010') and len(phone) == 11:
    print(f'{phone[-4:]:*>11}')
else:
    print('핸드폰번호를 입력하세요')
```

    *******0969
    

# 정중앙
> 사용자가 입력한 문자열중 가운데 글자를 출력하라. 문자열이 짝수라면 가운데 두글자를 출력하라


```python
text = input()
```

    qwerty
    


```python
# 아래에 코드를 작성하세요.
quo,rem = divmod(len(text),2)
if rem == 1:
    print(text[quo])
else:
    print(text[quo-1:quo+1])
```

    er
    
