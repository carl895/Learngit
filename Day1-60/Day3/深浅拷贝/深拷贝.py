from copy import deepcopy
lst = [1,2,[3,4,5]]
lst_deep = deepcopy(lst)
lst_deep[0] = 10
lst_deep[2][1] = 40
# 深拷贝验证
# 第一步 
# 返回False
print(lst[0] == lst_deep[0])
# 第二步
# 返回False
print(lst[2][1] ==lst_deep[2][1])
