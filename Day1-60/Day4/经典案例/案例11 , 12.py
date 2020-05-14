# 案例11样本抽样
from random import randint,sample,shuffle
lst = [randint(0,50) for _ in range(100)]
lst_sample = sample(lst,10)
# 案例12重洗数据集 shuffle函数能重洗数据，节省空间
shuffle(lst_sample)

print(lst_sample)


