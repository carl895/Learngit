# * 表示，后面的形参只能为关键字参数不能为位置参数
# / 前的参数只能是位置参数，不能是关键字参数。
len()

pow(x,y,z=None,/) # x ** y ，如果 z 给出，就取余：

round(number,[ndigits])# 四舍五入，ndigits指保留几位

sum(iterable,/,start= 0) #求和，start为初始值，结果相加

abs(x,/)#绝对值或复数的模

divmod(a,b)# 分别取商和余数

complex([real,[imag]]) # 创建一个复数
# complex(1,2) #(1+2j)