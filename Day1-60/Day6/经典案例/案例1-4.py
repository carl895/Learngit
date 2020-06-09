# 1.update 字典批量插入
d = {'a':1,'b':2}
d.update({'c':3,'d':4,'e':5})#法1
d.update([('c',3),('d',4),('e',5)])#法2
d.update([('c',3),('d',4)],e=5)#法3

# 2.setdefault
#字典中不存在某个键值对时，才插入到字典中
r =d.setdefault('c',3)#r=3
#如果存在，不必插入（也就不会修改键值对）
r =d.setdefault('b',22)#r=2

# 3.字典并集
def merge(d1,d2):
    return {**d1,**d2}
merge({'a':1,'b':2},{'c':3})
#{'a': 1, 'b': 2, 'c': 3}

# 4.字典差
def difference(d1,d2):
    return dict([(k,v) for k,v in d1.items() 
    if k not in d2])
difference({'a':1,'b':2,'c':3},{'b':2})
# {'a': 1, 'c': 3}