# 判断 list 内有无重复元素
def is_duplicated(lst):
    for x in lst:
        if lst.count(x) > 1:
           return True
    return False
a = [5,6,8,7,9,1,2]
print(is_duplicated(a))
# 以上方法实现不简洁，借助 set 判断更方便：  
#def is_duplicated(lst):
#    return len(lst) != len(set(lst))



