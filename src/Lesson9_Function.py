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

# #
# 函数的参数
# #

# #
# 位置参数
# 如前面使用的
# solutionToEquation(a,b,c)
# 其中 a,b,c 都是位置参数
# 因为参数的使用和确定是根据位置一一对应
# #

# #
# 默认参数
# 默认参数的意思是，该参数可以省略，省略时用默认值
# 也可以对 默认参数 幅值，这个参数会覆盖 默认参数
# 下面用 power 乘方函数来展示默认参数
# 默认参数要用不可变对象
# #

# def myPower(x,n=2) :
#     powerResult = 1
#     while n > 0 :
#         powerResult *= x 
#         n = n - 1
#     return powerResult

# power1 = myPower(2)
# power2 = myPower(2,10)
# print( power1,'\n',power2)

# #
# 可变参数（个数）
# 格式：多了一个 * 星号
# 这样会把输入组成一个 tuple
# 这样就可以直接输入多个值，或者直接输入 List 和 Tuple
# def functionName(*variable)
#     funtion_pass
# 以累加程序为例
# #

# def mySum(*num) :
#     sum = 0
#     for x in num :
#         sum += x
#     return sum
# >>> mySum(1,2,3)
# 6
# >>> mySum(*range(50))
# 1225

# #
# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
# 也就是说 关键字参数 可以传入一个 dict
# 定义： （多了 ** 两个星号）
# def functionName(variable1,**dictExample) :
#     function_pass
# 以成绩统计程序为例
# #

# >>> Score('Deng')
# name= Deng score= {}
# >>> Score('Deng',Math=100)
# name= Deng score= {'Math': 100}
# >>> newdict = {'Math':100,'Phisics':100}
# >>> Score('deng',**newdict)
# name= deng score= {'Phisics': 100, 'Math': 100}

# #
# 递归
# recursion
# 在一个函数的内部调用函数本身，就是递归函数
# 优点：逻辑清晰（所有的递归可以写成循环，但是循环的逻辑不如递归）
# 缺点：可能堆栈溢出
# 以 累乘 为例
# #

# >>> def fact(x):
# 	while x==1 :
# 		return 1
# 	return x*fact(x-1)

# >>> fact(10)
# 3628800

# #
# 联系：请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法，例如：
from Lesson9_Function_Hanoi import Hanoi
Hanoi(3)