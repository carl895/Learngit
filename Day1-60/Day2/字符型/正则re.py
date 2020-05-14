# 字符串的匹配操作除了使用 str 封装的方法外
# 还可用Python 的 re 正则模块功能更加强大

# 以 密码安全检查 为例：6到20位，只含数字字母
# 通配符匹配：(\w:含数字、字母、下划线)
#            (\d:数字0-9)
#            (\a-zA-Z:所有字母)

# 要求
import re
pat = re.compile(r'[\da-zA-Z]{6，20}')
pat.fullmatch('lym151AA')

