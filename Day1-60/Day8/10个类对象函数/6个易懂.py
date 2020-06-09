class Student():
    def __init__(self,id,name):
        self.id = id
        self.name = name
class undefgraduate(Student):
    pass

xiaoming = Student(1,'xiaoming')

# delattr(object,name) 删除属性
delattr(xiaoming, 'id')

# hasattr(object,name)判断是否还有删除的属性
hasattr(xiaoming,'id')

# getattr(object,name[,default]) 获取属性
getattr(xiaoming,'name')

# dir([object]) #不带参数时返回当前范围内的变量,方法和定义的类型列表；
# 带参数时返回参数的属性、方法列表。
dir(xiaoming)

# isinstance(object,classinfo)判断object是否为类classinfo的实例
isinstance(xiaoming,Student)
# 当序列类型的基类为 Iterable，返回True
from collections.abc import Iterable
isinstance([1,2,3],Iterable)#True

# issubclass(class,classinfo) 如果class是classinfo 类的子类
issubclass(undefgraduate,Student)#True
issubclass(object,Student)#False
issubclass(Student,object)#True
# classinfo 取值可能为元组，若class是元组内某个元素类型的子类则True
issubclass(int,(int,float))#True


