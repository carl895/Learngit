# copy 函数，仅仅实现对内嵌对象的一层拷贝，属于 shallow copy
lst = [1,2,[3,4,5]]
lst_shallow = lst.copy()
lst_shallow[0] = 10
lst_shallow[2][1] =40
# 浅拷贝验证

# 第一步
# 返回False，证明实现拷贝
print(lst[0] == lst_shallow[0])
# 第二步
# 返回True
print(lst[2][1] == lst_shallow[2][1])