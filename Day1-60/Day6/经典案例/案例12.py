# 重复最多
# 在两个列表中，找出重叠次数最多的元素，默认只返回一个

# 解决思路
# 1.交集
# 2.遍历交集列表中每一个元素，
# 利用比较min(元素在列表1的次数，列表2的次数)这就是重叠次数
# 3.求出重叠次数最多

def max_overlap(lst1,lst2):
    overlap = set(lst1).intersection(lst2)
    ox = [(x,min(lst1.count(x),lst2.count(x))) for x in overlap]
    return max(ox , key= lambda v: v[1]) #key= 是条件，表示看value

r = max_overlap([1,3,3,2,2,2,2],[3,3,2,2,2])
print(r)