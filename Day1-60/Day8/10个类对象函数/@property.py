#使用 Python 装饰器 @property，同样能实现对类上属性的定义 
#更简洁

class Student():
    def __init__(self):
        self._name =None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,val):
        self._name = val

    @name.deleter
    def name(self):
        del self._name

xiaoming = Student()
xiaoming.name = 'xiaoming'
print(xiaoming.name)