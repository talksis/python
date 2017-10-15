"""
1. 조건문 (if, elif, else) 
컴퓨터는 참과 거짓 만으로 판단을 하게 됩니다. 따라서 조건에 따라서 프로그램의 흐름을 바꿀때 사용합니다. 
예를 들어 사용자의 입력이 5보다 큰지 작은지에 대한 판단은 참과 거짓으로 나타낼 수 있습니다.
이와 같이 사용자의 입력에 따라서 프로그램의 흐름을 다르게 가져갈 수 있게 되는 것입니다. 
  
조건문은 다음과 같이 생각해도 됩니다.

__만약 이런 일이 발생하면, 이렇게 처리해줘__

또한 우리는 이런 조건들 안에 또 다른 조건을 삽입할 수 있습니다. 

__만약 이런 일이 발생하면, 이렇게 처리해줘__   
__그렇지 않고, 이런 일이 발생한다면 요렇게 처리해줘. __  
__그것도 아니라면 저렇게 처리해줘__  

이렇게 어떤 조건에 따라서 다른 동작을 요구해야 할 때 if문을 사용하게 됩니다. 그렇다면 파이썬 문법에서는 어떻게 처리할까요?
```python
if case1:
    action_1
elif case2:
    action_2
else:
    action_3
```
이때 주의해야 할 부분이 있습니다. if,elif 뒤에 공백이 존재합니다. 이 공백은 반드시 지켜져야 합니다. 또한 조건이 끝난 뒤에는 우리의 명령이 있어야 합니다. 따라서 조건과 명령을 구분하기 위해서 :을 사용합니다. 
또한 : 이 사용되고 난 다음줄에는 우리의 명령이 들어가게 되는데 이때 앞에 반드시 일정부분의 공백이 존재해야 합니다. 그래야만 이 조건에 따른 명령이 이곳이다 라는 것이 나타날 수 있겠죠.

"""

# if 문 기본

if True:
    print('if문은 조건이 참일 때 실행됩니다.')

if False:
    print('if문은 조건이 참일 때 실행됩니다.')

x = True

if x:
    print('x is True')
else:
    print('x is False')

x = False

if x:
    print('x is True')
else:
    print('x is False')


location = "school"

if location == 'bank' or location == 'school':
    print('this location is school')
elif location == 'bank':
    print('this location is bank')
else:
    print('where am i?')
