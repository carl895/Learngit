# 打印乘法表
def mul_table():
    for i in range(10):
        for j in range(1,i+1):
            print(str(j) + str('*') + str(i) + str('=') + str(i*j),end='\t')
        print()
mul_table()