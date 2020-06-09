# 调用对象的 repr() 方法，获得该方法的返回值
class Student():
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def __repr__(self):
        return 'id = '+self.id+',name = '+self.name+''

xiaoming = Student('001','xiaoming')
print(xiaoming)#id = 001, name = xiaoming
ascii(xiaoming)#'id = 001, name = xiaoming'