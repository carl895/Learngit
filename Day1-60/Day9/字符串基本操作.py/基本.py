# 反转字符串  两方法
s = 'python'
rs = ''.join(reversed(s))
rs #'nohtyp'
s[::-1] #'nohtyp'

# 字符串切片操作
java,python ="java","python"
jl,pl = len(java),len(python)# 4,6
[str(java[i % 3*jl :] + python[i % 5*pl] or i )
for i in range(1,10)] # i=3,6,9 为java i=5 为python 其余为i

#join 串联字符串
#split 分割字符串
#replace 方法替换
#strip 去前后空格

#子串判断
#判断a串是否为b串的字串  两方法
a ='our'
b ='flourish'
r = True if a in b else False
r # True
b.find(a) # 2

#字符串的字节长度
#encode 方法对字符串编码
def str_byte_len(mystr):
    mystr_byte  =mystr.encode('utf-8')
    return (len(mystr_byte))

str_byte_len('i love python')#13