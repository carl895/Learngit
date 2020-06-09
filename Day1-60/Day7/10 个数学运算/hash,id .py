# hash(object)返回对象的哈希值

class Student():
    def __init__(self,id,name):
        self.id = id
        self.name = name
    def __repr__(self):
        return 'id = '+self.id+',name = '+self.name+''

xiaoming = Student('001','xiaoming')
print(hash(xiaoming))

# id(object)# 返回对象的内存地址
print(id(xiaoming))