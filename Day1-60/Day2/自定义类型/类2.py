# 在属性不可访问(在name前加__)时：可property类就不用（.name()这样冗余）
class Dog(object):
    def __init__(self,name,dtype):
        self.__name = name
        self.__dtype = dtype
    @property
    def name(self):
        return self.__name
wangwang = Dog('wangwang','cute_type')
Dname = wangwang.name
print(Dname)