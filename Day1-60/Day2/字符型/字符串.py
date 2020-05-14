# 判断 str1 是否由 str2 旋转而来
# 转化为判断：str1 是否为 str2+str2 的子串

# 相关条件
def is_rotation(s1: str, s2: str) -> bool:
    if s1 is None or s2 is None:
        return False
    if len(s1) != len(s2):
        return False

    def is_substring(s1: str, s2: str) -> bool:
        return s1 in s2
    return is_substring(s1, s2 + s2 )

r = is_rotation('stringbook', 'bookstring')
print(r)