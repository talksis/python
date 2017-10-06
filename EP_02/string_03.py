'''
3. 문자열 인덱싱과 슬라이싱
문자열은 다양한 문자들의 집합입니다. 따라서 문자열 안에 있는 특정 문자에 접근할 수 있는 방법이 필요합니다.
따라서 문자열의 특정 문자에 접근하는 방법을 알아 봅시다.
문자열에서 인덱싱을 하기 위해서는 [] 기호를 사용합니다. 문자열에 접근하고 싶은 문자의 위치를 입력하게 됩니다.
이때 입력되는 자료는 숫자가 되며 문자의 순서라고 생각하면 됩니다.

또한 파이썬에서는 문자 뿐만 아니라 문자열의 부분 문자열까지도 접근할 수 있도록 설계되었습니다. 이를 슬라이싱이라고 합니다.
문자열은 [시작 위치:끝 위치] 기호를 사용합니다. 자료는 시작 위치, 끝 위치가 됩니다. 시작 위치와 끝 위치를 생략할 수 있는데, 생략하면, 시작위치는 처음이 되며
끝 위치는 문자열의 마지막 위치가 됩니다. 따라서 [:]는 문자열 전체가 됩니다.
또한 문자열을 건너뛰는 간격 및 방향을 설정할 수 있습니다. 다음과 같은 기호를 사용합니다 [시작 위치:끝 위치:간격 및 방향]
단, 한가지 예외사항이 있습니다. 만약 방향이 음의 방향인 경우(거꾸로 출력하는 경우) 시작 위치와 끝 위치는 바뀌어 출력하게 됩니다.
'''

### 문자열 인덱싱  - 1
s = 'Hello World'
print(s)
print( s[0] ) #결과값 H
print( s[4] ) #결과값 o
print( s[5] ) #결과값 공백

###   H   e  l  l  o     W  o  r  l  d
###   0   1  2  3  4  5  6  7  8  9 10
### -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

### 문자열 인덱싱 - 2
print( s[-1] )  #결과값 d
print( s[-11] ) #결과값 H
print( s[- 6] ) #결과값 공백

### 문자열 슬라이싱 - 1
print( s[1:] ) #결과값 ello World
print( s[:4] ) #결과값 Hell
print( s[2:8] ) #결과값 llo Wo  

### 문자열 슬라이싱 - 2
print( s[::1] ) #결과값 Hello World
print( s[-1:-12:-1] ) #결과값 dlroW olleH
print( s[0:10:-1] ) #결과값 

### 문자열 슬라이싱 - 3
print( s[::-1] ) #결과값 dlroW olleH
