# 斐波那契数列第一、二个元素都为 1，第三个元素等于前两个元素和
# 普通实现版本   n为几个数
def fibonacci(n):
    if n<= 1:
        return [1]
    fib = [1,1]
    while len(fib) < n:
        fib.append(fib[len(fib)-1] + fib[len(fib)-2])
    return fib

r = fibonacci(10)
print(r)
