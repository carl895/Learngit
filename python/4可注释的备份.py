import os 
import time


# 备份文件
source = 'C:\\Program1\\Git\\learngit\\python'
# 备份到下列目录
target_dir = 'D:\\code'

# 如果没有，则创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    print("sucessful created")

# 文件名 日期

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
target = today + os.sep + now + '.zip'

# 文件名注释
comment = input('enter command-->')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace('','_') + '.zip'


if not os.path.exists(today):
    os.mkdir(today)
    print("sucessful created")


# 打包成zip格式
rar_command = "WinRAR a %s %s"%(target,source) 


# 运行
print('rar command is ',rar_command)
print('running')
if os.system(rar_command) == 0:   
    print('sucessful backup to',target)
else:
    print('backup failed')


