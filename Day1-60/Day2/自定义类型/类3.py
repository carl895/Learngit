# 如果使 name 既可读又可写，就再增加一个装饰器 @name.setter
class Dog(object):
    def __init__(self,name,dtype):
        self.__name = name
        self.__dtype = dtype
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,new_name):
        self.__name = new_name # 可以新起名字
wangwang = Dog('wangwang','cute_type')
# 新名字
wangwang.name = wangwang2.0

Dname = wangwang.name
print(Dname)