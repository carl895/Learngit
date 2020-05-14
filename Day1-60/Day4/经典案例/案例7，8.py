# 案例7
# 求表头 返回第一个元素，当列表为空时，返回None
def head(lst):
    return lst[0] if len(lst)>0 else None

print(head([]))
print(head([4,3,5]))


# 案例8  
# 求表尾 同上
def tail(lst):
    return lst[-1] if len(lst) >0 else None

print(tail([]))
print(tail([4,3,5]))