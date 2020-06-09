#集合是一种不允许元素出现重复的容器

#借助集合这种数据类型来
#判断一个列表中是否含有重复元素
def duplicated(lst):
    return len(lst) != len(set(lst))
