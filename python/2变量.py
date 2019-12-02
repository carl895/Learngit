# 局部变量
x = 50


def func(x):
    #全局变量加global x
    print("x is", x)
    x = 2
    print("Changed local x to",x)

func(x)
# 同2
print("'Value of x is",x)