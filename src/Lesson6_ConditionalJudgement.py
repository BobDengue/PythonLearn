# #
# 条件判断还是比较简单的 
# 注意缩进和 :
# #

# #
# 格式1
# 条件为布尔表达式，为真时执行
# if <条件> ：
#     <执行>
# #

# #
# 格式2
# if <条件> ：
#     <执行1>
# else :
#     <执行2>
# #

# #
# 格式3
# if <条件1> ：
#     <执行1>
# elif <条件2> ：
#     <执行2>
# elif <条件3> ：
#     <执行3>
# else :
#     <执行4>
# #

# #
# 习题：小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
# #

height = float( input( 'Plz input your height ' ))
weight = float( input( 'Plz input your weight ' ))
BMI = weight *weight /height
print('your BMI is %2.2f' % BMI)
if BMI < 18.5 :
    print('过轻')
elif BMI < 25 :
    print('正常')
elif BMI < 28 :
    print('过重')
elif BMI < 32 :
    print('肥胖')
else:
    print('严重肥胖')
