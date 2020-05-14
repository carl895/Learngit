class Dog(object):
    def __init__(self,name,dtype):
        self.name = name
        self.dtype = dtype
    def shout(self):
        print('I \'m %s ,type: %s'% (self.name,self.dtype))
wangwang = Dog('wangwang','cute_type')
Dname = wangwang.name 
print(Dname)
# 属性name可被修改
wangwang.name = 'wrong_name'
