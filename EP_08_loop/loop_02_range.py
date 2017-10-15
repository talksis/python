'''
2. for문을 위한 도구 range
range는 하나의 함수입니다. range는 자동으로 숫자로 이루어진 리스트를 반환합니다.(python2기준) . 형식이 조금 특이한데 다음과 같은 형식입니다.abs

__range( stop )__  
__range( start, stop[, step])__  

처음 형식은 조금 낮설수 있으나, 두번째 형식은 우리가 연속된 자료형태에서 슬라이싱과 비슷합니다. 이를 사용하여 for문을 좀 더 
효과적으로 사용해 봅시다.
'''


### range 함수의 사용 - 1

# my_list = list(range(10))
# print(my_list)

### range 함수의 사용 - 2
# my_list = list(range(5,10))
# print(my_list)

### range 함수의 사용 - 3
# my_list = list(range(0,10,2))
# print(my_list)


### for 문과 range 함수의 조합

for i in range(10):
    print(i)