# property(fget=None ,fset=None ,fdel=None ,doc=None)
# 返回property 属性 ，不适用装饰器

# 定义类上的属性：
class Student():
    def __init__(self):
        self._name =None

    def get_name(self):
        return self._name

    def set_name(self,val):
        self._name = val

    def del_name(self):
        del self._name

    # 显示 调用 property 函数 
    name = property(get_name,set_name,del_name,"name property")

xiaoming = Student()
xiaoming.name ='xiaoming'

print(xiaoming.name)

