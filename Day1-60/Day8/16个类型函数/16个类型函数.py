bool([x]) #测试对象是True 还是False
bool([])#False      有元素就是True


bytes([source[,encoding[,errors]]])
#将一个字符串转换成字节类型
s = 'apple'
bytes(s,encoding='utf-8')#b'apple'


str(object='') 
int(x,base = 10)#后面的参数为进制
float(x)


chr(i) #查看十进制整数对应的ASCll字符


ord(c) #查看ASCll字符对应的十进制整数


object() #返回一个根对象，它是所有类的基类
o =object
type(o) #object
o.__dir__() # 查看object对象上的所有方法

type(object) #查看对象的类型


frozenset([iterable]) #创建不可修改的冻结集合，
#一旦创建不允许增删元素
#而普通集合set创建后仍可修改 add  pop

set([iterable]) #返回一个集合对象，并允许修改元素
#集合优点 容器里不允许重复
a =[1,4,5,2,1]
set(a)#{1,2,4,5}

dict() #{}  # 中的zip()合并字典
#class dict(**kwarg)
#class dict(mapping, **kwarg)
#class dict(iterable, **kwarg)

tuple([iterable])#不可修改的元组对象

list([iterable])
#使用map函数
m =map(lambda i: str(i),[186,1256,3521])
l = list(m) #['186','1256','3521']
#相似的例子
list(map(lambda x: x%2==1,[1,3,2,4,1]))
[True,True,False,False,True]


range(stop) range(start,stop,step)

slice(stop) slice(start,stop,step)
a =[2,4,5,3,1]
a[slice(0,5,2)] #等价为a[0:5:2]
#元素为 [2,5,1]


zip(*iterables) #创建一个迭代器，聚合每个可迭代对象的元素
#参数前带 *，意味着是可变序列参数,可传入1，2，或多个
#传入1个
for i in zip([1,2]):
    print(i)# (1,) (2,)
#传入2个
a = range(5)
b = list('abcde')
[str(y) + str(x) for x,y in zip(a,b)]
#['a0','b1','c2','d3','e4']
