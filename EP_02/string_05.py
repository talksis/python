'''
5. 문자열 메소드
파이썬에서는 문자열에 대해서 내장된 메소드들을 제공합니다. 이를 사용하면 문자열에 대한 조작은 더욱 쉽게 해줍니다.
모든 메소드를 설명할 수 없지만 유용한 것들을 알아봅시다.
'''

### 문자열의 + *

s1 = 'Hello '
s2 = 'World '
s = s1 + s2
print(s) #결과값 'Hello World' 

s = s1 * 5 + s2 * 2
print(s) #결과값 'Hello Hello Hello Hello Hello World World'


### upper 모든 문자를 대문자로 변환, lower 모든 문자를 소문자로 변환

s = 'Hello'
print(s.upper()) #결과값 'HELLO'
print(s.lower()) #결과값 'hello'
print(s) #결과값 'Hello

### split 문자열을 잘라 리스트로 반환

s = 'Hello World. I am a newbie'
print(s.split(' ')) #결과값 ['Hello', 'World.', 'I', 'am', 'a', 'newbie']
print(s) #결과값 'Hello World. I am a newbie'

### replace 특정 문자열 치환하기

s = 'Hello World. I am a newbie'
print(s.replace('I am', 'You are')) #결과값 Hello World. You are a newbie
print(s.replace('l','x',2)) #결과값 Hexxo World. You are a newbie
print(s)

### count 특정 문자 세기
s = 'Hello World. I am a newbie'
print(s.count('l')) #결과값 3

### find, index 특정 문자의 위치 알려주기

s = 'Hello World. I am a newbie'
print(s.find('l')) #결과값 2
print(s.find('x')) #결과값 -1
print(s.index('l')) #결과값 2
print(s.index('x')) #오류 발생