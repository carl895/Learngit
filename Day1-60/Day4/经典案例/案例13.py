# 生成满足均匀分布的坐标点
from random import uniform
x ,y = [i for i in range(10)],[
    round(uniform(0, 10), 2) for _ in range(10)]
print(y)