"""
4. 문자열 format 심화

문자열을 다루다보면 우리가 출력하고 싶은 정보를 출력하기에 번거로운 부분이 있을 수 있습니다. 이를 위해서 + 기호를 사용하고 end 의 값을 변경할 수 있지만,
문자열 자체를 우리가 원하는 문자열로 바꾸어 출력하는 방법도 생각해 볼 수 있습니다. 이를 위해서 문자열 메소드 중 format 메소드가 존재합니다.abs

**str.format(*args, **kwargs)**
<https://docs.python.org/3/library/stdtypes.html#str.format>
format 메소드에서도 *과 **이 존재하는데 이 부분에 대해서는 함수 관련 강좌에서 자세히 설명하도록 하고 이번 시간에는 format을 사용하여 문자열을 쉽게 고쳐보도록 합시다.

"""

### format 사용 - 위치를 활용한 방법

print('{0}, {1}, {2}'.format('a', 'b', 'c')) #출력값 a, b, c
print('{}, {}, {}'.format('a', 'b', 'c')) #출력값 a, b, c
print('{2}, {1}, {0}'.format('a', 'b', 'c')) #출력값 c, b, a
print('{2}, {1}, {0}'.format(*'abc')) #출력값 c, b, a
print('{0}{1}{0}'.format('abra','cad')) #출력값 abracadabra

### format 사용 - 이름을 활용한 방법

print('당신의 이름은 {user_name} 입니다. 당신의 점수는 {total_score} 입니다.'.format(user_name="박성준",total_score=69))


### format 정렬 및 공간

print( '{:<30}'.format('좌측 정렬'))
print( '{:>30}'.format('우측 정렬'))
print( '{:^30}'.format('가운데 정렬'))
print( '{:*^30}'.format('가운데 정렬'))

### format 실수 출력

print('{:+f} {:+f}'.format(3.14, -3.14))
print('{: f} {: f}'.format(3.14, -3.14))
print('{:-f} {:-f}'.format(3.14, -3.14))


### format 다양한 진법에 따른 출력
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))
print("int: {0:#d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42))

### format 3자리씩 , 찍기

print( '{:,}'.format(1234567890) )

### format 퍼센트로 표현하기
print('{:.2%}'.format(19/22))
