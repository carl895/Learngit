# 更长集合(多者)

def longer(s1,s2):
    return max(s1,s2 ,key=lambda v: len(v))

r = longer({1,2,3,4,5},{1,3,5,7})
print(r)