# 找出列表中的所有重复元素
# 并添加到ret
def find_duplicate(lst):
    ret  = []
    for x in lst:
        if lst.count(x) >1 and x not in ret:
            ret.append(x)
    return ret

r = find_duplicate([1,5,6,8,5,6,4,2,5,8,1])
print(r)