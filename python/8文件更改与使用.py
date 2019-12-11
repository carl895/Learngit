f =open('poem.txt')
while True:
    line = f.readline()
    # 零长度指示 EOF 未知？
    if len(line) == 0:
        break
    # 遍历所有
    for line in f:
        print(line)
    # 关闭文件
f.close()