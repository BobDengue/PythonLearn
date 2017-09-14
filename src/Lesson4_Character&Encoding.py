# #
# python 使用 Unicode 编码，与 ASCII 类似
# 取字符的编码 ord
# ord('邓')
# 37011
# 取编码对应的字符 chr
# chr(37011)
# '邓'
# #

# #
# 编码与译码
# encode & decode
# 比如在 ASCII 中，A的编码是65
# 'A' 'ABC' 是一个字符串chr
# b'A' b'ABC' 是一个bytes，每个字符只占用一个字节
# 例如：
# 'ABC'.encode('ASCII')
# 输出 b'ABC'
# c= b'ABC'.decode('utf-8')
# 输出 ABC
# 为了理解 'ABC' 与 b'ABC' 的差异 , 使用 len 函数
# c = len ('邓')
# d = len ('邓'.encode('utf-8'))
# print('c=',c)
# print('d=',d)
# 输出 c= 1    d= 3
# 也就是说：'邓' 只是一个字符 ， 但是在 utf-8 编码中 ，'邓'占了三个字节
# #

# #
# 格式控制
# %d 整数
# %f 浮点数
# %s 字符串
# %x 十六进制
# 例如：
# print('The utf-8 encode of %s is %d' % ('A',ord('A')))
# The utf-8 encode of A is 65 
# 当需要输出 % 百分号时使用 %%
# print('%s %%' % 's')
# s %
# print('%%')
# %%
# 不确定时可以都用%s w(ﾟДﾟ)w 
# #

# 为了让自己和别人了解文件的编码，一般如下注释
# -*- coding: utf-8 -*-

# 习题：小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
score1=int(input('Please input the first score '))
score2=int(input('Please input the second score '))
scoreChangeRatio = score2 / score1 - 1  
print('The score has changed from %d to %d by the ratio of %2.1f%%' % (score1,score2,scoreChangeRatio*100))
