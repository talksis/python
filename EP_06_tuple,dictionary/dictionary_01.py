"""
1. Dictionary (dict)의 정의와 생성
딕셔너리는 특이한 구조로 되어 있습니다. 키와 값의 구조로 저장되는 형태입니다. 일반적으로는 맵이라고 부르기도 합니다. 
딕셔너리의 특이한 점은 키는 불변하며(immutable) 값은 가변적(mutable)입니다. 따라서 하나의 키에 해당하는 값을 바꿀 수 있지만,
키 자체를 바꾸는 것은 불허합니다. 
따라서 잘 생각해 보면, 키로 사용될 수 있는 것에 튜플을 사용해 됩니다. 튜플은 불변하니까요. 하지만 리스트는 키로 사용할 수 없다는 결론에 도달합니다.
하지만 초기에는 딕셔너리에 키를 튜플로 사용할 일은 거의 없다고 봐도 됩니다. 

딕셔너리는 다음과 같은 기호를 통해 나타냅니다. 
__{}__
"""

### 딕셔너리의 생성

my_dict ={}
my_dict = dict()
my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
my_dict = { '배트맨':90, '아이언맨':93, '슈퍼맨':74}
my_dict = dict(key1='value1', key2='value2')
my_dict = dict([('key1','value2'),('key2','value2')])