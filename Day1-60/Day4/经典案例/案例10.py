# 元素对
# t[:-1]：原列表切掉最后一个元素；
# t[1:]：原列表切掉第一个元素；
# zip(iter1, iter2)：实现 iter1 和 iter2 的对应索引处的元素拼接。
# 例子
# In : list(zip([1,2],[2,3]))
# Out：[(1,2),(2,3)]

def pair(t):
    return list(zip(t[:-1],t[1:]))
    
print(pair([1,2,3]))
print(pair(range(5)))


