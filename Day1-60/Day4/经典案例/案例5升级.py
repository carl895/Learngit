# 支持返回多个
def mode(lst):
    if lst is None or len(lst)==0:
        return None
    max_freq_elem = max(lst,key= lambda v: lst.count(v))
    max_freq = lst.count(max_freq_elem)
    ret = []
    for i in lst:
        if i not in ret and lst.count(i)==max_freq:
            ret.append(i)
    return ret

r = mode([1,2,5,3,2,1,2,1])
print(r)