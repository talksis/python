"""
3. list의 수정(mutable) (삭제 및 추가)
문자열은 불변객체이기 때문에 수정할 수 없었습니다. 하지만, 리스트는 수정가능한 객체로 각 객체에 접근하여 그 내용을 수정할 수 있습니다. 
객체를 수정하는 방법에 대해서 알아봅시다.
"""

### index를 이용하여 내용 수정

my_list = [1,2,3,4,5]
my_list[3] # 결과값 4
my_list[3]=10 
my_list #결과값 [1,2,3,10,5]

### slice 를 이용하여 내용 수정

my_list = [1,2,3,4,5] 
my_list[1:3] #결과값 2,3
my_list[1:3] = 10 #에러 발생
#TypeError: can only assign an iterable
my_list[1:3] = [10] 
my_list #결과값 1,10,4,5


### append 메소드를 이용하여 추가하기

my_list = [1,2,3,4,5]
my_list.append(10)
my_list  #결과 [1,2,3,4,5,10]
my_list.append(['리스트를','추가합시다'])
my_list  #결과 [1,2,3,4,5,10,['리스트를','추가합시다']]
my_list.append(3,4) #에러 발생. append는 1개의 인자만을 갖게 됩니다.

### insert 메소드를 사용하여 추가하기
my_list = [1,2,3,4,5]
my_list.insert(3,10)
my_list #결과 [1,2,3,10,4,5]

### pop 메소드를 사용하여 삭제하기
my_list = [1,2,3,4,5]
my_list.pop() #결과 5
my_list #결과 [1,2,3,4]
my_list.pop() #결과 4
my_list #결과 [1,2,3]

my_list.pop(1) #결과 2
my_list #결과 [1,3]

### del 을 사용하여 객체 삭제하기

my_list = [1,2,3,4,5]
del my_list[2]
my_list #결과 [1,2,4,5]
del my_list[2:4] 
my_list #결과 [1,2]


### remove를 사용하여 객체 삭제하기

my_list= [1,2,3,4,5]
my_list.remove(2)
my_list #결과 [1,3,4,5]
my_list.remove(2) #에러 발생


### 연산자를 이용한 수정 (+ , *)

my_list1 = [1,2,3,4,5]
my_list2 = [6,7,8,9,10]

my_list1 += my_list2