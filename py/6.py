# 漂亮打印
import pprint

message = 'I love zhangyaqi'
count = {}
for i in message:
    count.setdefault(i,0)
    count[i] = count[i] + 1
pprint.pprint(count)     
# pprint.pformat(count)     如果想要得到打印的文本作为字符串，而不是显示在屏幕上