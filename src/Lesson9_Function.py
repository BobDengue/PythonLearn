# -*- coding: utf-8 -*-

# #
# 函数的调用
# python 自带的函数查看
# https://docs.python.org/3/library/functions.html
# function(参数)
# 参数的数量或者类型错误
# python 会报 TypeError 错误
# 并提示错误信息
# #

# #
# 函数的定义
# def functionName(Variable...)
#     function
# 注意 return
# 在 return 执行之后，函数就结束运行了
# 省略 return ，其实执行的是 return none
# 同时 return none <=> return 
# 已经编写了 Lesson9_Function_muAbs.py
# 其中有 myAbs() 函数
# 调用如下
# #

# from Lesson9_Function_myAbs import myAbs
# c = myAbs('a')
# print(c)

# #
# 空函数
# pass
# pass 通常用来做占位符，程序不报语法错误
# #

# def nop():
#     pass

# #
# 类型检查
# 报错均是
# typeError
# 一是：参数个数的检查
# 二是：参数类型的检查
# 编写的时候要注意这两点
# #

# #
# return 的返回值是一个 tuple
# 也就是说可以用一个变量来存储这个 tuple
# 如果用多个变量来存储的话
# 就是 tuple 对对应位置的变量赋值
# #

# from Lesson9_Function_mySinAndCos import sinAndCos
# c = sinAndCos(0)
# print(c)
# # angle = input('Input angle : ')

# s,c = sinAndCos(45)
# print(s)
# print(c)
# # 0.8509035245341184
# # 0.5253219888177297

# 练习 ：请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0
# 的两个解。

# from Lesson9_Function_SolutionToEquation import solutionToEquation
# a = float( input('Input a : '))
# b = float( input('Input b : '))
# c = float( input('Input c : '))
# root = solutionToEquation(a,b,c)
# print(root)