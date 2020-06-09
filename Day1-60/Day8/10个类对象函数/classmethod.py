# classmethod 修饰符对应的函数不需要实例化，不需要 self 参数

# 第一个参数需要是表示自身类的 cls 参数，
# 能调用类的属性、方法、实例等

class Student():
    def __init__(self,id=None,name=None):
        self.id = id
        self.name= name
    
    def instance_method(self):
        print('这是实例方法')
        return self
    
    @classmethod
    def __annotations__(cls):
        return '学生类'

    @classmethod
    def print_type_name(cls):
        print('这是类上的方法，类名为 %s，注解为 %s '
        % (cls.__name__,cls.__annotations__()))

Student().print_type_name()
Student().instance_method()