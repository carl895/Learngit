import re

#5. re.I 忽略大小写
s3 ='That'
pat4 = r't'
r =re.finditer(pat4,s3,re.I)

print([i.span() for i in r])#[(0,1),(3,4)]

#6. split 分割单词
#简单的分割就不用re.split
#复杂的可用   \s为匹配空白字符
s4 = 'This,,,   module ; \t   provides|| regular ; '
word =re.split(r'[,\s;|]+',s4)
print(word)
# ['This', 'module', 'provides', 'regular', '']

#7. sub替换匹配串
#与replace类似
conte = 'hello 123456,hello 654321'
pat =re.compile(r'\d+')#要替换的是数字
m =pat.sub('666',conte)   #（新，旧）  replace（旧，新）
print(m)#'hello 666,hello 666'

#8. compile预编译
lst = [-16,'good',1.5, 0.2, -0.1,0, '11.43', 10, '0.1111']
rec = re.compile(r'^[1-9]\d*\.\d*|0\.\d*[1-9]\d*$')

print([i for i in lst if rec.match(str(i))])


#9. 贪心捕获
content = '''
        <h>ddeng</h>
          <div>graph</div>
        <div>math</div>'''
result =re.findall(r"<div>(.*)</div>",content) #(.*) 表示捕获任意多个字符，尽可能多地匹配字符，也被称为贪心捕获   . 表示匹配除换行符外的任意字符。
print(result)

#10.这种匹配模式串 (.*?)，被称为非贪心捕获


# 十个正则表达式核心要点
# 1.search
# 2.match
# 3.finditer
# 4.findall
# 5.re.I
# 6.split
# 7.sub
# 8.compile
# 9.贪心捕获
# 10.非贪心捕获    9. 10.  一样？
