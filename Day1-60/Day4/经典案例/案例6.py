# 更长列表
def max_len(*lists):
    return max(*lists, key= lambda v: len(v))

r = max_len([1,2,3,4],[5,6,7],[8])
print(f'更长列表：{r}')