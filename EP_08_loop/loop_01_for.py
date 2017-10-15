'''
1. loop (for문)
for를 사용하는 루프는 파이썬에서 반복을 위해 사용됩니다. 
파이썬은 조금 특이하게 연속된 자료의 형태(리스트, 문자열, 튜플,사전 등)와 같이 반복이 가능한 자료형태들에 대해 동작합니다.
파이썬의 for 루프는 다음과 같은 형태를 갖습니다.

```python3
for item in object:
    statements
```

이때 아이템의 이름을 여러분이 알기 쉬운 것으로 정하는 것이 좋습니다. 나중에 코드를 다시 읽었을 때, 그 내용을 파악하기 쉽게 하기 위함입니다.

'''

### 리스트의 반복

# my_list = [1, 2, 3, 4, 5]

# for element in my_list:
#     print(element)


### 리스트의 반복을 이용한 짝수 추출
# my_list = [1, 2, 3, 4, 5]
# for num in my_list:
#     if num % 2 == 0:
#         print('{} 짝수입니다'.format(num))
#     else:
#         print('{} 홀수입니다.'.format(num))


### 리스트의 반복을 이용한 합의 계산
# my_list = [1, 2, 3, 4, 5]
# list_sum = 0
# for num in my_list:
#     list_sum = list_sum + num
# print(list_sum)


### 문자열의 반복

# my_string = 'Hello World!, this is python!'

# for letter in my_string:
#     print(letter)

### 튜플의 반복
# my_tuple = (1, 2, 3, 4, 5)
# for item in my_tuple:
#     print(item)


### 반복에서의 아이템이 반복가능한 경우

# my_list = [(2, 4), (6, 8), (10, 12)]

# for tup in my_list:
#     print(tup)

# for first, second in my_list:
#     print('first is {} , second is {}'.format(first,second))

# for tup in my_list:
#     for item in tup:
#         print(item,end=' ')
#     print()

### 딕셔너리의 반복

# my_dict = dict(k1a=40, k2a=50, k3a=60)

# for key in my_dict:
#     print(key, type(key))

