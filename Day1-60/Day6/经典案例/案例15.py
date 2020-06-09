# 15.逻辑上合并字典
# 案例3的升级版
# dic1 = {'x': 1, 'y': 2 }
# dic2 = {'y': 3, 'z': 4 }
# merged = {**dic1, **dic2} 
# 修改merged['x']=10  dic1是不变的

# 案例15
from collections import ChainMap 
#它在内部创建了一个容纳这些字典的列表
dic1 = {'x': 1, 'y': 2 }
dic2 = {'y': 3, 'z': 4 }
merged =ChainMap(dic1,dic2)
print(merged)

merged['x'] = 10
print(merged)