# callable(object)
# 判断对象是否可被调用，
# 能被调用的对象就是一个 callable 对象
# 比如函数 str、int 等都是可被调用的。
callable(str)#True

# xiaoming 实例不可被调取

#如果xiaoming 能被调用：
#必须重写Student 类上__call__方法

class Student():
    def __init__(self,id ,name):
        self.id = id
        self.name = name
    def __call__(self):
        print('I can be called')
        print(f'my name is {self.name}')

t = Student('001','xiaoming')

t()
