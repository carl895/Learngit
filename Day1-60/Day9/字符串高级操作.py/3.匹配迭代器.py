# finditer方法,返回所有子串匹配位置的迭代器

s = '山东省潍坊市青州第1中学高三1班'
pat = '1'
r = re.finditer(pat,s)
for i in r:
    print(i)

#<re.Match object; span=(9, 10), match='1'>
#<re.Match object; span=(14, 15), match='1'>