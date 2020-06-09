# 最大的字典值
# 可能有多对

def max_value(d):
    if len(d) == 0:
        return []
    m_value = max(d.values())
    return [(key, m_value) for key in d
    if d[key] == m_value]

r = max_value({'e':8,'c':4,'f':8})
print(r)