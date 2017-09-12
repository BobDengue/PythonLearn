#python 能够直接处理的数据类型

##
# 整数
# 999
# 1010
# 0xfff
# #

##
# 浮点
# 1.1
# 1e9
# 1.23e9
# #

# #
# 字符串
# 使用单引号 '' 或者双引号 "" 括起来的文本
# 在 '' & “” 中使用 ' & " 字符，需要使用转义字符 \ ，例如：
# print('R\'u ok?')
# 输出 R'u ok?
# 常见转义字符 ： \t => tab ; \n => enter ; \\ => \
# 禁用转义字符 r'' ,例如
# print(r'R\'u ok?')
# 输出 R\'u ok?
# '''...'''格式使用在换行中，例如
# print('A\nB\nC')
# <=> 
# print('''A
# B
# C''')
# #

# #
# 布尔值,仅有两个值
# True , False 
# 真，假
# 运算有
# and , or ,not
# 与，或，非
# 常用于条件判断中
# #

# #
# 空值 
# None
# #

# #
# 变量
# 动态语言，不要定义变量的类型，可以反复幅值，如
# a=123
# print(a)
# a= 'ABC'
# print(a)
# #

# #
# 常量
# python 中不存在常量，通常保持一个量不变使用大写来提醒不要修改，例如：
# PI=3.1415926
# #

# #
# 另外，有 / 和 //(整除) 两种除法
# print(10/3)
# 3.3333333333333335
# print(10//3)
# 3
# print(10%3)
# 1
# #

# #
# 练习：输出下列字符
# n = 123
# f = 456.789
# s1 = 'Hello, world'
# s2 = 'Hello, \'Adam\''
# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,
# Lisa!'''
# #
# print('n = 123 \nf = 456.789 \ns1 = \'Hello, world\' \ns2 = \'Hello, \\\'Adam\\\'\' \ns3 = r\'Hello, \"Bart\"\' \ns4 = r\'\'\'Hello, \nLisa!\'\'\'')
# 用 '''   ''' 改进一下
print('''n = 123 
f = 456.789 
s1 = \'Hello, world\' 
s2 = \'Hello, \\\'Adam\\\'\' 
s3 = r\'Hello, \"Bart\"\' 
s4 = r\'\'\'Hello, 
Lisa!\'\'\'''')