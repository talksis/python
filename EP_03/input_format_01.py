"""
1. 사용자 입력 함수

input 함수는 사용자의 키보드 입력을 위한 함수입니다. input을 활용하여 콘솔상태에서 사용자의 키보드 입력을 받아 처리할 수 있습니다. 
다만, input을 활용하여 데이터를 입력받게 되면 그 자료를 모두 문자열로 처리하게 됩니다. 따라서 이를 적절히 변환하는 방법 역시 같이 배워보도록 합시다.
사용자 입력을 받기 위해서는 다음의 함수를 사용합니다.

**input()**

하지만 위의 함수를 바로 적용시켜 보면 커서만 깜빡거리게 됩니다. 이는 사용자의 입력을 받을 수 있는 대기 상태를 말하지만, 사용자의 입장에서는 어떤 정보를 입력해야 하는지 알지 못합니다.
따라서 일반적인 경우에는 사용자에게 어떤 정보를 입력받아야 하는지 명시하도록 구성됩니다.

**input( 사용자에게 보여줄 문자열 )**

그리고 이제부터는 Python3 공식 사이트의 문서에 표현된 방식으로 설명을 이어나가도록 하겠습니다.
따라서 다음과 같이 input 함수는 사용됩니다.

**input( [prompt] )**
<https://docs.python.org/3/library/functions.html#input>

이때 [] 안에 있는 내용은 생략이 가능한 내용이며, prompt에 보여줄 내용이라는 뜻이 됩니다. 
"""

### input 함수 - 문자열 입력
input('당신의 이름을 입력하세요.')  
input('당신의 이름을 입력하세요\n->')

user_name = input('당신의 이름을 입력하세요.\n->')

print('당신의 이름은')
print(user_name)
print('입니다')


### input 함수 - 정수 입력
total_score = input('당신의 총점을 입력하세요. ->')
total_sub = input('과목의 수를 입력하세요. ->')
print(total_score/total_sub) #에러 발생

#TypeError: unsupported operand type(s) for /: 'str' and 'str'

total_score = int( input('당신의 총점을 입력하세요. ->') )
total_sub = int( input('과목의 수를 입력하세요. ->') )
print(total_score/total_sub) 

### input 함수 - 문자열, 정수 모두 입력 받았을 때의 연산

user_name = input('당신의 이름을 입력하세요->')
total_score = int( input('당신의 총점을 입력하세요->'))
print('당신의 이름은 ' + user_name +' 입니다. 당신의 총점은 '+total_score+' 입니다') #에러 발생
# print('당신의 이름은 ' + user_name +' 입니다. 당신의 총점은 '+total_score+' 입니다')
#TypeError: must be str, not int

print('당신의 이름은 ' + user_name +' 입니다. 당신의 총점은 '+str(total_score)+' 입니다') 


### eval 함수를 통한 데이터 입력

user_name = eval(input("당신의 이름은->"))
total_score= eval(input("당신의 총점을 입력하세요->"))
print('당신의 이름은 ' + user_name +' 입니다. 당신의 총점은 '+str(total_score)+' 입니다') 
