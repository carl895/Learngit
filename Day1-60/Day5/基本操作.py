#1创建字典
d = {'a':1,'b':2,'c':3}
#2遍历字典
for key,val in d.items():
    print(key,val)
#3获取所有键集合（keys）
set(d)
set(d.keys)
#4获取所有值集合（values）
set(d.values)
#5获取某键对应的值
d.get('c')
#6添加、修改或删除一个键值对
d['d']=4
#法1
del d['d']
print(d)
#法2
d.pop('c')
print(d)