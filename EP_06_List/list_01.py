"""
1. 리스트의 생성
우리가 자료를 다루다 보면 하나의 변수에 담기에는 불편한 부분들이 있습니다. 여러 자료가 한꺼번에 들어있어야 하는 경우를 생각해 봅시다. 
자신의 자산을 관리하는 프로그램을 작성한다고 생각해 봅시다. 지출내용을 모두 변수에 하나씩 담기에는 매우 번거로운 일입니다.
따라서 여러 자료를 한꺼번에 저장하고  위한 자료형이 있습니다. 바로 리스트(List)입니다. 간단히 여러 자료가 한꺼번에 들어 있는 자료형이라고 생각하면 쉽습니다.
리스트는 다음의 기호를 사용합니다.abs
__[]__
파이썬에서는 위와 같은 기호를 사용하게 되면 리스트 자료형으로 인식하게 됩니다. 
"""

### 리스트 생성

numbers = [1,2,3,4,5,6,7,8,9,10] 
strings = ['배트맨', '슈퍼맨', '아이언맨', '헐크', '원더우먼'] 
mixed_type1=[10, '배트맨', 20, '슈퍼맨'] 
mixed_type2=[10, 20, 3.14 ,['배트맨', '슈퍼맨', '아이언맨']] 
empty_list1 = list()
empty_list2 = []

len(mixed_type2) # 결과값 4 




