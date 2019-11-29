# 由于函数多了一个参数，要使 power（x）正常使用，必须加个默认值n=2
def power(x, n):
    s = 1
    while n > 0:
        n = n-1
        s = s * x
    return s
print(power(5,3))