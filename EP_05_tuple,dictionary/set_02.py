'''
2. set의 추가 삭제 

set에서는 추가 삭제를 메소드를 통해서 할 수 있습니다. 따라서 기본 메소드와 함께 알아봅시다.
'''

### set의 원소 추가 add와 update

# my_set = set()
# print( my_set ) #결과 {}
# my_set.add(1) 
# print( my_set ) #결과 {1}
# my_set.update({1,2,3,4,5})
# print( my_set ) #결과 {1,2,3,4,5}

### set의 원소 삭제 remove, pop, clear

my_set={1,2,3,4,5}
my_set.remove(1)
print( my_set ) #결과 {2,3,4,5}
# my_set.remove(1) #에러 발생
my_set.discard(2)
my_set.discard(2)
print( my_set ) #결과 {3,4,5}

print( my_set.pop() ) #결과 랜덤...

