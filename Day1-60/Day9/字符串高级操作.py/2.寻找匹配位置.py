# 使用正则模块
import re
# match 从原字符串开始位置进行匹配 
#（必须是字符串的第一个字符开始，不然都为None）
s = 'ourself'
recom = re.compile('our')
r1 = recom.match(s)
print(r1)#(0,3)

#search 任意位置
pat = 'our'
r = re.search(pat,s)
print(r.span()) #(0,3)


