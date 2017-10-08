"""
3. dictionary 의 유용한 메소드 
딕셔너리의 유용한 메서드들을 알아보도록 하겠습니다.abs
"""

### get 을 이용한 자료의 출력

# my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
# print( my_dict.get('key1') ) #결과 'value1'
# print( my_dict.get('key10') ) #결과 None
# print( my_dict.get('key10','empty') ) #결과 'empty'

### pop 을 이용한 삭제 

# my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
# print( my_dict.pop('key1') ) #결과 'value1'
# print( my_dict.pop('key1') ) #에러 발생

### popitem을 이용한 삭제

# my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
# print( my_dict.popitem() ) #tuple 형태의 key value가 반환 결과 ('key3','value3')
# print( my_dict.popitem() ) #tuple 형태의 key value가 반환 결과 ('key2','value2')
# print( my_dict.popitem() ) #tuple 형태의 key value가 반환 결과 ('key1','value1')
# print( my_dict.popitem() ) #에러 발생
# # KeyError: 'popitem(): dictionary is empty'

### keys 함수를 이용한 키 추출
# my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
# print( my_dict.keys()[0] ) #결과 dict_keys(['key1', 'key2', 'key3'])
# print( list(my_dict.keys()) ) #결과 ['key1', 'key2', 'key3']

### values 함수를 이용한 값 추출
# my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
# print( my_dict.values() ) #결과 dict_values(['value1', 'value2', 'value3'])
# print( list(my_dict.values()) ) #결과 ['value1', 'value2', 'value3']

### items 메소드를 이용한 키, 값 형태의 추출
# my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
# print( my_dict.items() ) #결과 dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])
# print( list(my_dict.items()) ) #결과 dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')])

### update를 활용한 여러 값의 추가 및 수정
# my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
# my_dict.update({'key1':'newValue1', 'key10':'New Key and Value'})
# print( my_dict ) #결과 {'key1': 'newValue1', 'key2': 'value2', 'key3': 'value3', 'key10': 'New Key and Value'}