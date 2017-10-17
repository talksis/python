'''
2. set의 연산
set은 집합과 같기 때문에 연산이 가능합니다. 이때 주의해야 할 것은 집합의 기준으로 생각해야 한다는 것입니다.
기본적으로 합집합, 교집합, 차집합 과같은 연산이 지원 됩니다.
'''

### set의 합집합
set_1 = {1,2,3}
set_2 = {3,4,5}

set_3 = set_1 | set_2
print( set_3 ) #결과 {1,2,3,4,5}
set_3 = set_1.union(set_2)
print( set_3 ) #결과 {1,2,3,4,5}

### set의 교집합
set_1 = {1,2,3}
set_2 = {3,4,5}

set_3 = set_1 & set_2
print( set_3 ) #결과 {3}
set_3 = set_1.intersection(set_2)
print( set_3 ) #결과 {3}

### set의 차집합
set_1 = {1,2,3}
set_2 = {3,4,5}

set_3 = set_1 - set_2
print( set_3 ) #결과 {1,2}
set_3 = set_1.difference(set_2)
print( set_3 ) #결과 {1,2}

set_1 = {1,2,3}
set_2 = {3,4,5}
set_1.intersection_update(set_2)
print(set_1)