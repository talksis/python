"""
2. 딕셔너리 값의 읽기 추가 삭제 수정
딕셔너리는 문자열, 리스트, 튜플과는 다르게 키와 값의 형태로 저장됩니다. 따라서 인덱싱과 슬라이싱이 존재하지 않습니다. 키와 값의 형태를 사용하는 이유는 키를 이용하여 빠르게 자료에 접근하는 것이 가능하기 때문입니다.
값을 읽는 방법은 간단히 키를 부르면 값이 출력되는 방식을 사용하고 있습니다. 따라서 필수적으로 키는 중복되면 안됩니다. 
"""

###  키를 통해 값 읽기

my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
print( my_dict['key1'] ) #결과 'value1'
print( my_dict['key10'] ) #에러 발생
#KeyError: 'key1'


### 자료의 추가 
my_dict[1] = '추가한 값입니다.'
print( my_dict[1] ) #결과 'value1'

### 자료의 수정
my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
my_dict['key2'] = 3
print( my_dict )  #결과 {'key1': 'value1', 'key2': 3, 'key3': 'value3'}

### 자료의 삭제 
my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
del my_dict['key1']
del my_dict['key1'] #에러 발생
#KeyError: 'key1'