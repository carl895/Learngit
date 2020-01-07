# 正向 与 反向  （2、3、 12-27复制的）
import re
import string

def reverse(text):
    return text[::-1]

def inputtext(text):
#   text = text.lower()
#   text = text.replace(" ","")    
#   return text == reverse(text)
    text0 = clear(text)
    return text0 == reverse(text0)

# 将数据的字符串中的空白字符和标点符号
def clear(text):
    # 去掉字符串中的空白字符
    text1 = re.sub('\s','',text)
    bytes_tabtrans = bytes.maketrans(b'abcdefghijklmnopqrstuvwxyz', b'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    # 此为中文标点符号
    punc = "！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏."
    # string.punctuation 此为英文标点符号
    mark=''.join([punc,string.punctuation])
    bytes1 = mark.encode(encoding='utf-8',errors='strict')
    bytestr = text1.encode(encoding='utf-8',errors='strict')
    # 去掉字符串中的标点符号
    return (bytestr.translate(bytes_tabtrans,bytes1)).decode("utf-8")


something = input("Enter text:")
if inputtext(something):
    print("yes",end='')
else:
    print("no")
