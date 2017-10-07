'''
4. 문자열의 수정 불가능(immutable)
다른 언어와는 다르게 파이썬의 문자열은 수정불가능 객체라고 합니다. 이를 immutable이라고 부릅니다.
만약 문자열을 수정한다면 새로운 객체가 생성되게 됩니다.
새로운 객체가 생성된다는 의미를 지금 이해하기는 어렵습니다만 간단한 예제를 통해 알아보겠습니다.abs
'''

### 수정 불가능

s = 'Hello World'
s[3] = 'x' # 에러

"""
    s[3] = 'x'
TypeError: 'str' object does not support item assignment
"""

### 슬라이싱을 이용하여 문자열 수정하기

s = 'Hello World'
s = s[:3] + 'x' + s[4:]
print(s) #결과값 'Helxo World'

### 문자열을 수정했을 때 새로운 객체의 생성

s = 'Hello World'
s2 = s
s = 'New Hello World'
print(s) #결과값 'New Hello World'
print(s2) #결과값 'Hello World'
