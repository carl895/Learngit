# super([type[,object-or-type]])
# 返回一个代理对象，它会将方法调用委托给 type 的父类或兄弟类。
# 子类的 add 方法，一部分直接调用父类 add，
# 再有一部分个性的行为：打印结果。

class Parent():
    def __init__(self,x):
        self.v = x
    
    def add(self,x):
        return self.v + x  # 1 + 2 

class Son(Parent):
    def add(self,y):
        r = super().add(y)
        print(r)
        #负责打印

Son(1).add(2)