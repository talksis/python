"""
1. boolean 
프로그래밍에서는 참과 거짓은 매우 중요합니다. 디지털이라는 것은 0과 1의 값을 말하죠. 컴퓨터는 디지털 기기 입니다. 따라서 0과 1로만 말을 하는 기계입니다.
따라서 컴퓨터는 참과 거짓만으로 이루어진 기계이며 컴퓨터를 다루는 프로그래밍에서 참과 거짓은 매우 중요합니다.
우리의 상식으로 크다 작다 같다와 같은 내용은 참과 거짓이 명확합니다. 하지만 프로그래밍상에서 참과 거짓은 약간 다르게 사용될 수 있습니다. 
그런데 참과 거짓을 잘 생각해 보면, 한쪽 경우를 확실하게 알게 된다면 반대쪽 역시도 확실히 아는 것이 됩니다. 즉, 거짓의 경우를 확실하게 알게 된다면, 자연스럽게 그에 해당하지 않는 경우는 참이 된다는 것을 알 수 있죠.

프로그래밍에서 참과 거짓이 어떤 경우 나타나는지 확인해 봅시다.
이를 위해서 
__bool__ 함수를 사용합시다.
bool( 값 ) 을 넣게 되면 이 안에 값이 참인지 거짓인지 판단해 줍니다.abs

"""

### 파이썬에서의 참과 거짓

True #참
False #거짓

### 파이썬에서의 참과 거짓을 구분짓기 (거짓)

False
None
0 
''
()
[]
{}

falses = (False,None,0,'',[],(),{})
for i in falses:
    print(bool(i))


