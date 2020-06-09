# 一键对多值字典
#法1常规思路
d ={}
lst = [(1,'apple'),(2,'orange'),(1,'computer')]
for k,v in lst:
    if k not in d:
        d[k]=[]
    d[k].append(v)
print(d)