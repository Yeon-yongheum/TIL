
# 모든코인 상승장? 하락장?
> 최고가와 최저가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 최고가 보다 높을 경우 "상승장", 그렇지 않은 경우 "하락장" 문자열을 출력하라.


|Key Name|Description|
|------|---|
|opeing_price|최근 24시간 내 시작 거래금액|
|closing_price|최근 24시간 내 마지막 거래금액|
|min_price|최근 24시간 내 최저 거래금액|
|max_price|최근 24시간 내 최고 거래금액|


```python
import requests
import pprint
url = "https://api.bithumb.com/public/ticker/all"
data = requests.get(url).json()['data']
del data['date']
#pprint.pprint(data)
for k,v in data.items():

    if float(v['opening_price']) + float(v['max_price']) - float(v['min_price']) > float(v['max_price']):
        print(f'{k}는 상승장')
    else :
        print(f'{k}는 하락장')
            
            
            
```

    BTC는 상승장
    ETH는 상승장
    DASH는 상승장
    LTC는 상승장
    ETC는 상승장
    XRP는 상승장
    BCH는 상승장
    XMR는 상승장
    ZEC는 상승장
    QTUM는 상승장
    BTG는 상승장
    EOS는 상승장
    ICX는 상승장
    VET는 상승장
    TRX는 상승장
    ELF는 상승장
    MITH는 상승장
    MCO는 상승장
    OMG는 상승장
    KNC는 상승장
    GNT는 상승장
    ZIL는 상승장
    ETHOS는 상승장
    PAY는 상승장
    WAX는 상승장
    POWR는 상승장
    LRC는 상승장
    GTO는 상승장
    STEEM는 상승장
    STRAT는 상승장
    ZRX는 상승장
    REP는 상승장
    AE는 상승장
    XEM는 상승장
    SNT는 상승장
    ADA는 상승장
    PPT는 상승장
    CTXC는 상승장
    CMT는 상승장
    THETA는 상승장
    WTC는 상승장
    ITC는 상승장
    TRUE는 상승장
    ABT는 상승장
    RNT는 상승장
    PLY는 상승장
    WAVES는 상승장
    LINK는 상승장
    ENJ는 상승장
    PST는 상승장
    SALT는 상승장
    RDN는 상승장
    LOOM는 상승장
    PIVX는 하락장
    INS는 상승장
    BCD는 상승장
    BZNT는 상승장
    XLM는 상승장
    OCN는 상승장
    BSV는 상승장
    TMTG는 상승장
    BAT는 상승장
    WET는 상승장
    XVG는 상승장
    IOST는 상승장
    POLY는 상승장
    HC는 상승장
    ROM는 상승장
    AMO는 상승장
    ETZ는 상승장
    ARN는 상승장
    APIS는 상승장
    MTL는 상승장
    DACC는 상승장
    DAC는 상승장
    BHP는 상승장
    BTT는 상승장
    HDAC는 상승장
    NPXS는 상승장
    AUTO는 상승장
    GXC는 상승장
    ORBS는 상승장
    VALOR는 상승장
    CON는 상승장
    ANKR는 상승장
    MIX는 상승장
    HYC는 상승장
    LBA는 상승장
    


```python
# 풀이
import requests
import pprint
url = "https://api.bithumb.com/public/ticker/all"
data = requests.get(url).json()['data']
#print(data)
for coin, coin_data in data.items():
    if type(coin_data) != type(dict()):
        continue
    else:
        if float(coin_data['opening_price'])-float(coin_data['min_price']) > 0:
            print('상승장')
        else:
            print('하락장')
    
```

    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    하락장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    상승장
    

# 평균점수
> 다음 딕셔너리에서 평균 점수를 출력하라



```python
student = {'python':80, 'algorithm':78, 'django':95, 'flask':80}
total = 0
for sub,score in student.items():
    total = score + total
print(total/len(student))

```

    83.25
    


```python
#풀이 1
count = 0
total_score = 0
for key in student:
    total_score += student[key]
    count += 1
print(total_score/count)


```

    83.25
    


```python
#풀이 2
sum(student.values())/len(student)
```




    83.25




```python
list(student.values())
```




    [80, 78, 95, 80]



# 혈액형
> 학생들의 혈액형(A,B,O,AB)에 대한 데이터가 리스트에 들어있다. 각 혈액형이 몇명인지 딕셔너리를 만들어 출력하라


```python
blood = ['A','A','B','O','A','B','A','AB','AB','O','A','O','AB','O']
A_count = 0
B_count = 0
O_count = 0
AB_count = 0
for string in blood:
    if string == 'A':
        A_count += 1
    elif string == 'B':
        B_count += 1    
    elif string == 'O':
        O_count += 1        
    elif string == 'AB':
        AB_count += 1    
print (f'A형은 {A_count}명, B형은 {B_count}명, O형은 {O_count}명,AB형은 {AB_count}명,')
```

    A형은 5명, B형은 2명, O형은 4명,AB형은 3명,
    


```python
# 풀이1
c= []
a = 0
b = 0
ab = 0
o = 0

print(blood.count('A'))
a = c.append(blood.count('A'))
b = c.append(blood.count('B'))
o = c.append(blood.count('O'))
ab = c.append(blood.count('AB'))

d = ['A','B','O','AB']
print(dict(zip(d,c)))
```

    5
    {'A': 5, 'B': 2, 'O': 4, 'AB': 3}
    


```python
# 풀이2
blood_dict = {}
# (반복)하나씩 꺼내서 확인한다.
for blood_type in blood:
#    print(blood_type)
    #지금 나온적이 없으면, 키와 value1로 만든다.
    if blood_type not in blood_dict.keys():
        blood_dict[blood_type] = 1
    else:
        blood_dict[blood_type] += 1
print(blood_dict)
```

    A
    A
    B
    O
    A
    B
    A
    AB
    AB
    O
    A
    O
    AB
    O
    {'A': 5, 'B': 2, 'O': 4, 'AB': 3}
    


```python
{blood_type: blood.count(blood_type) for blood_type in set(blood)}
```




    {'A': 5, 'AB': 3, 'B': 2, 'O': 4}




```python
blood.count('A')
```




    5



# UBD
> movies는 영화제목이 key로 누적관객수가 value인 딕셔너리이다. 
>
> 자전차왕 엄복동의 누적관객수는 172212명이고 172212명을 1UBD라고 할때 80UBD를 넘지 못하는 영화를 출력하라.


```python
movies = {
    "7번방의선물":12811206,
    "괴물":13019740,
    "국제시장":14257115,
    "극한직업":16261018,
    "도둑들":12983330,
    "명량":17613682,
    "베테랑":13414009,
    "신과함께-죄와벌":14410754,
    "아바타":13624328,
    "어벤져스:엔드게임":13901423,
}
UBD = 172212

for name,person in movies.items():
    print(person/UBD)
    if person/UBD <80:
        print(name)
```

    74.3920632708522
    7번방의선물
    75.60297772512949
    괴물
    82.78816226511509
    94.42441873969294
    75.39155227278006
    도둑들
    102.27906301535317
    77.89241748542494
    베테랑
    83.68031263791141
    79.11369707105196
    아바타
    80.72273128469561
    
