"""
4. 리스트의 관련 메소드
리스트는 다앙한 메소드를 사용할 수 있습니다. 아주 간단한 조작만으로 우리가 필요한 정보를 찾을 수 있는 도구가 됩니다.
주의깊게 보아야 할 점은 문자열과는 다르게 리스트는 수정 가능하다는 것으로 인하여 리스트 메소드의 일부는 리스트 자체를 조작해서 원래와는 다른 수정된 자료가 되는 경우가 많습니다.
따라서 원래의 자료를 보존해야 하는지, 아닌지를 판단하여 사용하여야 합니다.
"""

### max
my_list = [1,2,3,4,5]
max(my_list) #결과 5

### min
my_list = [1,2,3,4,5]
min(my_list) #결과 1

### count 
my_list = [1,2,3,4,5]
my_list.count(2) #결과 1


### reverse 

my_list = [1,2,3,4,5]
my_list.reverse()
my_list #결과 [5,4,3,2,1]

### sort

my_list = [2,5,1,4,3]
my_list.sort()
my_list #결과 [1,2,3,4,5]
my_list.sort(reverse=True)
my_list #결과 [5,4,3,2,1]


