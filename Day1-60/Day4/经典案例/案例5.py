# 出镜最多  利用py内置函数max函数 此方法默认只返回一个
def mode(lst):
    if lst is None or len(lst)==0:
        return None 
    return max(lst, key= lambda v : lst.count(v))

lst = [1,3,5,3,1,1]
r = mode(lst)
print(f'{lst} 中出现次数最多的元素{r}')
