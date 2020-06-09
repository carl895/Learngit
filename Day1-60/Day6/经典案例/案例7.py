# 最大键(比键)
# 通过 keys 拿到所有键，获取最大键，
# 返回 (最大键,值) 的元组

def max_key(d):
    if len(d) == 0:
        return []
    m_key = max(d.keys())
    return (m_key,d[m_key])

r = max_key({'c':5,'e':8,'a':3}) 
print(r)    