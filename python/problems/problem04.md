
# `abs()`

> 절대값은 숫자(int, float)가 들어오면 절대값을 반환하고, 복소수(complex)가 들어오면 그 크기를 반환합니다.
> 
> `my_abs(x)`를 만들어보세요.

**공식문서**
<center>
    <img src="https://user-images.githubusercontent.com/52446416/61273106-b6ee5c00-a7e3-11e9-8ec2-a086b0bc584f.png", alt="">
</center>

**복소수 크기 구하는법**
<center>
    <img src="https://user-images.githubusercontent.com/52446416/61273105-b655c580-a7e3-11e9-9859-0a9ffdecdf7d.png", alt="">
</center>


```python
# 예제 입력 및 출력
print(abs(3+4j), abs(-0.0), abs(-5))
```

    5.0 0.0 5
    


```python
# 아래에 코드를 작성해주세요.
def my_abs(a):
    if type(a) == complex:
        return (a.real**2 + a.imag**2)**(1/2)
    else:
        if a > 0 :
            return a
        elif a == -0:
            return 0
        elif a < 0 :
            return -a

```


```python
# 예제 입력 및 출력
print(my_abs(3+4j))
print(my_abs(-0.0))
print(my_abs(-5))
print(my_abs(-5.123))
```

    5.0
    0.0
    5
    5.123
    


```python
# 풀이
def my_abs(number):
    # 복소수 일때,
#     if type(number) == type(-1+1j):
#         return '복소수입니다.'
    if isinstance(number, complex):
        return (number.real**2 + number.imag**2)**(1/2)
    # 실수 및 정수일 떄,
    if number == 0:
        return number**2
    elif number > 0:
        return number
    else:
        return -number
    
```

# 문자열 탐색

> 문자열 요소로만 이루어진 리스트를 넣었을 때, 문자열 길이가 2 이상이고 주어진 문자열의 첫번째와 마지막 문자가 같은 문자열의 수를 세는 함수 `start_end`를 작성하시오.

예시)

```python
start_end(['level', 'asdwe', 's', 'abceda', 'gsdwrtfg']) #=> 3
```



```python
# 여기에 코드를 작성하세요.
def start_end(words):
    count = 0
    for elem in words:
        if elem[0] == elem[-1] and len(elem) >= 2:
            count += 1
    return count
```


```python
# 해당 코드를 통해 3이 나오는지 확인하세요.
print(start_end(['level', 'asdwe', 's', 'abceda', 'gsdwrtfg']))
```

    3
    


```python
# 풀이 
def start_end2(words):
    # 통을 만든다.
    count = 0
    # 리스트를 반복하면서
    for word in words:    
        # 만약에, len(문자영ㄹ) >= 2 and 첫번째/두번째 같은지
        if word[0] == word[-1] and len(word) >= 2:
            count += 1
    # 해당하는 길이 리턴
    return count
print(start_end2(['level', 'asdwe', 's', 'abceda', 'gsdwrtfg']))
```

    3
    


```python
def start_end3(words):
    return len([word for word in words if word[0] == word[-1] and len(word) >= 2])

print(start_end3(['level', 'asdwe', 's', 'abceda', 'gsdwrtfg', 'aswea']))
```

    4
    


```python
a = 'asdf'
print(len(a))
print(a[-1] == a[0])

```

    4
    False
    

# Collatz 추측

> 1937년 Collatz란 사람에 의해 제기된 이 추측은, 주어진 수가 1이 될때까지 다음 작업을 반복하면, 모든 수를 1로 만들 수 있다는 추측입니다. 작업은 다음과 같습니다.
>
> 1. 입력된 수가 짝수라면 2로 나눕니다. 
> 2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
> 3. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.
>
> 예를 들어, 입력된 수가 6이라면 6→3→10→5→16→8→4→2→1 이 되어 총 8번 만에 1이 됩니다.
>
> 위 작업을 몇 번이나 반복해야하는지 반환하는 함수, `collatz`를 완성해 주세요.
>
> 단, 작업을 500번을 반복해도 1이 되지 않는다면 –1을 반환해 주세요.

예시)

```python
collatz(6) #=> 8
collatz(16) #=> 4
collatz(27) #=> 111
collatz(626331) #=> -1
```


```python
# 여기에 코드를 작성하세요.
def collatz(n):
    count = 0
    for i in range(500):
        if n%2:
            n = n*3+1
            count += 1
        else:
            n = n/2
            count += 1
            if n == 1:
                return count
    return -1
```


```python
# 해당 코드를 통해 8, 4, 111, -1 이 나오는지 확인하세요.
print(collatz(6))
print(collatz(16))
print(collatz(27))
print(collatz(626331))
```

    8
    4
    111
    -1
    


```python
# 풀이
def collatz(number):
    count = 0
    # 500번 시행
    for i in range(500):
        # 홀수
        if number%2:
            number = number*3 + 1
        # 짝수
        else:
            number = number / 2
        # 1이 되면 종료(return)
        if n == 1:
            return i + 1 #0~499니까
    # 500번 해도 없으면 -1 반환
    return -1
```


```python
def collatz(number):
    for i in range(500):
        number = (number*3 + 1) if number%2 else (number / 2)
        if number == 1:
            return i + 1
    return -1
print(collatz(6))
print(collatz(16))
print(collatz(27))
print(collatz(626331))
```

    8
    4
    111
    -1
    

# 무엇이 중복일까

> 다음 리스트에서 중복되는 요소만 뽑아서 새로운 리스트를 반환하는 `duplicated` 함수를 작성하세요 옮기시오. 

```python
# 입력)
duplicated(['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'b'])

# 출력)
['b', 'n']
```


```python
# 여기에 코드를 작성하시오.
def duplicated(chars):
    list1 = []
    for i in range(len(chars)):
        print(chars)
        if chars[i] in chars[i+1:] and chars[i] not in list1:
            list1.append(chars[i])
            print(list1)
    return list1       
```


```python
# 해당 코드를 통해 올바른 결과가 나오는지 확인하세요.
duplicated(['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'b'])
```

    ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'b']
    ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'b']
    ['b']
    ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'b']
    ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'b']
    ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'b']
    ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'b']
    ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'b']
    ['b', 'n']
    ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'b']
    ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'b']
    




    ['b', 'n']




```python
# 풀이
def duplicated(chars):
    # 결과 통 
    result = []
    # 하나씩 확인하면서,
    for char in chars:
    #중복을 확인하고 결과에 없으면 넣는다.
        if chars.count(char) > 1 and char not in result:
            result.append(char)
    return result

print(duplicated(['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'b']))
```

    ['b', 'n']
    


```python
def duplicated(chars):
    return len({char for char in chars if chars.count(char) > 1})
print(duplicated(['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'b']))
```

    2
    


```python
c = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n', 'b']

print(c[0:10:2])
```

    ['a', 'c', 'd', 'n', 'b']
    
