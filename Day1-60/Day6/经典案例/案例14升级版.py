# 半懂
# 更加方便
# 使用 collections 模块 中 defaultdict
# 它能创建属于某个类型的自带初始值的字典
from collections import defaultdict
lst = [(1,'apple'),(2,'orange'),(1,'compute')]
d= defaultdict(list)
for k,v in lst:
    d[k].append(v)

print(d)