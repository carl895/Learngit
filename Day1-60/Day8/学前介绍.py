# 函数作用域问题

# 遇到变量作用域的问题
# 有全局变量，局部变量等
# Python 查找变量的顺序遵守 LEGB 规则
# 即遇到某个变量时:

# L优先从它所属的函数（local）内查找；
# E若找不到，并且它位于一个内嵌函数中，就再到它的父函数（enclosing）中查找；
# G如果还是找不到，再去全局作用域（global）查找；
# B再找不到，最后去内置作用域（build-in）查找。
# 还找不到报错。

a = 10
def parent():
    b = 20
    def son():
        c = 30 # c: local 
        print(b + c) # b: enclosing
        print(a + b + c ) # a: global
        print(min(a,b,c)) # min : built-in 
    son()
parent()