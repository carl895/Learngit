# 计算字符出现次数
message = 'I love you'
count = {}
for i in message:
    count.setdefault(i,0)
    count[i] = count[i] + 1
print(count)    