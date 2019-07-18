
# `all()`

> all은 인자로 받는 iterable(range, list)의 모든 요소가 참이거나 비어있으면 True를 반환합니다.
>
> 이와 같은 my_all(x)을 작성해보세요


```python
# 예제 입력 및 출력
print(all([1, 2, 5, '6']))
print(all([[], 2, 5, '6']))
print(all([]))
print(all('d'))

```

    True
    False
    True
    True
    


```python
# 아래에 코드를 작성해주세요.
def my_all(a):   #lsit 한개만 받음
    for i in a:
        if i:
        #if bool(i) == True:
            continue
        else:
            return False
    return True

```


```python
# 예제 입력 및 출력
print(my_all([1, 2, 5, '6']))
print(my_all([ 2,[], 5, '6']))
print(my_all([]))
print(all('d'))
```

    True
    False
    True
    True
    


```python
# 풀이
def my_all(x):
    # 원소를 하나씩 확인해서,
    for element in x:
        # False가 있다면
        if not element:
            # return False
            return False
    # 다 끝났으면, False가 없다라는 것이니까 return True
    return True
```


```python
# 예제 입력 및 출력
print(my_all([1, 2, 5, '6']))
print(my_all([ 2,[], 5, '6']))
print(my_all([]))
print(all('d'))
```

    True
    False
    True
    True
    


```python
if not [1]:
    print ('hi')
else:
    print('bye')
```

    bye
    

# `any()`

> any는 인자로 받는 iterable(range, list)의 요소 중 하나라도 참이면 True를 반환하고, 비어있으면 False를 반환합니다.
>
> 이와 같은 my_any(x)를 작성해보세요.


```python
# 예제 입력 및 출력
print(any([1, 2, 5, '6']))
print(any([[], 2, 5, '6']))
print(any([0]))
```

    True
    True
    False
    


```python
# 아래에 코드를 작성해주세요.
def my_any(a):
    for i in a:
        if i:
            return True
    return False
```


```python
# my_any 예제 입력 및 출력
print(my_any([1, 2, 5, '6']))
print(my_any([2, [], 5, '6']))
print(my_any([0]))
```

    True
    True
    False
    


# 이상한 덧셈

> 숫자들을 받아서 양의 정수의 합을 구하는 함수 `positive_sum`을 작성하세요.

예시)

```python
positive_sum(1,-4,7,12) #=> 20
positive_sum(-1, -2, -3, -4) #=> 0
```


```python
# 여기에 코드를 작성하세요.
def positive_sum(*num):
    sum1 = 0
    for i in num:
        if i >= 0:
            sum1 += i
    return sum1
```


```python
# 해당 코드를 통해 20과 0이 나오는지 확인하세요.
print(positive_sum(1,-4,7,12))
print(positive_sum(-1, -2, -3, -4))
```

    20
    0
    


```python
def positive_sum(*num):
    #결과 통
    sum1 = 0
    #원소하나씩 확인
    for i in num:
        #양수면
        if i >= 0:
            #더해라
            sum1 += i
    #결과반환
    return sum1
```


```python
def pos_sum(*num):
    return sum([num for num in num if num > 0])
```


```python
# 풀이
print(pos_sum(1,-4,7,12))
print(pos_sum(-1, -2, -3, -4))
```

    20
    0
    
