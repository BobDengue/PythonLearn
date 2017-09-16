# def myAbs(x) :
#     if x <= 0:
#         return -x
#     else:
#         return x

# 带有类型检查
def myAbs(x) :
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x <= 0:
        return -x
    else:
        return x