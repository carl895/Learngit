# 单字符串
# 字符串中不出现相同的字符，则被称为单字符串

def single(string):
    return len(set(string)) == len(string)

r1 =single('python')
r2 =single('love_python')#相同的有o
print(r1)
print(r2)