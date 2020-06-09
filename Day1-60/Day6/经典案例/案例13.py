# topn 键
#找出字典前 n 个最大值，对应的键
#导入Python 内置模块 heapq 中的 nlargest 函数，获取字典中的前 n 个最大值
from heapq import nlargest
def topn_dict(d,n):
    return nlargest(n,d,key=lambda k: d[k]) #key 函数定义按值比较大小：

r =topn_dict({'a':5, 'b':4, 'c':5, 'd':6},3)
print(r)