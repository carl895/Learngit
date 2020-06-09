# 案例5按键排序
def sort_by_key(d):
    return sorted(d.items(),key=lambda x: x[0])
    #x[]解释为参数x为元素（key，value）
# sorted函数返回列表，元素为tuple
r =sort_by_key({'a':3,'c':1,'b':2})
print(r) #[('a',3),('c',1),('b',2)]

# 案例6按值排序
def sort_by_value(d):
    return sorted(d.items(),key=lambda x: x[1])
    #x[]解释为参数x为元素（key，value）
# sorted函数返回列表，元素为tuple
r =sort_by_value({'a':3,'c':1,'b':2})
print(r) #[('c',1),('b',2),('a',3)]
