
# 불쌍한 달팽이

>달팽이는 낮 시간 동안에 기둥을 올라갑니다. 하지만 밤에는 잠을 자면서 어느 정도의 거리만큼미끄러집니다. (낮 시간 동안 올라간 거리보다는 적게 미끄러집니다) 달팽이가 기둥의 꼭대기에 도달하는 날까지 걸리는 시간을 계산하면 됩니다.

> 함수에 들어가야 하는 3개의 인자는 다음과 같습니다.
- 기둥의 높이(미터)
- 낮 시간 동안 달팽이가 올라가는 거리(미터)
- 달팽이가 야간에 잠을 자는 동안 미끄러지는 거리(미터)

```python
snail(100, 5, 2)
# => 33
```


```python
# 여기에 코드를 작성하세요
def snail(a,b,c):
    day = 0
    while True:
        # 날짜를 카운트
        day += 1
        # 낮에 가야할 높이가 낮아짐
        a = a - b
        # 올라 갔는지 확인
        if a < 0:
            return day
        # 밤에 가야할 높이가 높아짐
        a = a + c
        print(a,end=(' '))
        
    return day
```


```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
print(snail(100, 5, 2))
print(snail(100, 7, 5))
```

    97 94 91 88 85 82 79 76 73 70 67 64 61 58 55 52 49 46 43 40 37 34 31 28 25 22 19 16 13 10 7 4 33
    98 96 94 92 90 88 86 84 82 80 78 76 74 72 70 68 66 64 62 60 58 56 54 52 50 48 46 44 42 40 38 36 34 32 30 28 26 24 22 20 18 16 14 12 10 8 6 48
    

# 편-안한 단어

> (QWERTY 키보드를 사용하여 타이핑을 한다고 가정할 때) '편안한 단어'는 타이핑 할 때 **손을 번갈아 칠 수 있는 단어**를 말합니다.
>
> 단어를 인자로 받아 그것이 '편안한 단어'인지 여부를 True/False로 반환하는 함수를 만드세요.(모든 단어는 a ~ z까지 오름차순으로 구성된 문자열입니다.)

> 문자 목록
- 왼손: q, w, e, r, t, a, s, d, f, g, z, x, c, v, b
- 오른손: y, u, i, o, p, h, j, k, l, n, m


```python
# 여기에 코드를 작성하세요.
def comfortable_word(word):
    left = 'qwertasdfgzxcvb'
    right = 'yuiophjklnm'
    for i in range(1, len(word)):
        if ((word[i] in left) and (word[i-1] in right)) or ((word[i] in right) and (word[i-1] in left)):
            continue
        else:
            return False
    return True
```


```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
print(comfortable_word('qywu'))
print(comfortable_word('apple'))
print(comfortable_word('qkskflrp'))
```

    True
    False
    True
    


```python
# 문제 풀이
def comfortable_word(word):
    # 왼손 문자 목록, 오른손 문자 목록
    left_word = 'qwertasdfgzxcvb'
    right_word = 'yuiophjklnm'
    # 하나씩 반복하는데, 필요한것은 이전 문자의 왼쪽인지 오른쪽인지의 여부
    is_left = True if word[0] in left_word else False # 초기값을 지정
    for char in word[1:]:
        # 만약에 이전 것이 왼쪽이고, 지금 단어가 왼쪽이면 종료
        if is_left and char in left_word:
            return False
        # 오른쪽 - 오른쪽이면 종료(False)
        if not is_left and char in right_word:
            return False
        is_left = not is_left
    # 종료 안되었으면 True
    return True
        
```


```python
print(comfortable_word('qywu'))
print(comfortable_word('apple'))
print(comfortable_word('qkskflrp'))
```

    True
    False
    True
    


```python
print(comfortable_word('kqkskflrp'))
```

    True
    

# 숫자패턴

>원하는 행까지 아래의 패턴을 생성하는 함수를 작성하세요. 만약 인자가 0이나 음의 정수인 경우 빈 문자열('')로 반환하세요.
> 
> 짝수가 인수로 전달되면 패턴은 통과된 짝수보다 작은 최대 홀수까지 계속되어야 합니다.

```python
# 예시 
print(pattern(9))
1
333
55555
7777777
999999999

print(pattern(6))
1
333
55555
```
**유의!**
패턴에 공백은 없습니다.


```python
# 여기에 코드를 작성하세요
def pattern(num):
    if num <= 0:
        return ''
    if not num%2:
        num = num -1
    for p in range(1,num+1,2):
        q = str(p)
        print(q*p)
    return ''
```


```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
print(pattern(9))
print(pattern(6))
print(pattern(-1))
```

    1
    333
    55555
    7777777
    999999999
    
    1
    333
    55555
    
    
    


```python

def pattern(number):
    if number <= 0:
        return ''
    # 문자열 통
    result = ''
    
    for i in range(1,number+1):
        if i % 2:
            result += str(i)*i
            if i != number:
                result += '\n'
    return result
```


```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
print(pattern(9))
print(pattern(6))
print(pattern(-1))
```

    1
    333
    55555
    7777777
    999999999
    1
    333
    55555
    
    
    


```python
def pattern(number):
    return '\n'.join([str(i)*i for i in range(1,number+1) if i%2 ]) if number > 0 else ''
```


```python
print(pattern(9))
print(pattern(6))
print(pattern(-1))
```

    1
    333
    55555
    7777777
    999999999
    1
    333
    55555
    
    


```python
def pattern(number):
    return '\n'.join([str(i)*i for i in range(1,number+1,2)]) if number > 0 else ''
```


```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
print(pattern(9))
print(pattern(6))
print(pattern(-1))
```

    1
    333
    55555
    7777777
    999999999
    1
    333
    55555
    
    


```python

```
