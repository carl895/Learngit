# 去掉列表中的一个最小值和一个最大值后，计算剩余元素的平均值
def score(lst):
    lst.sort()
    lst2 = lst[1:-1]
    return round((sum(lst2)/len(lst2)),2)

lst = [9.8 , 8.4 , 9.5 , 7.9 , 8.8 , 9.4 , 7.4 , 6.4]
print(score(lst))