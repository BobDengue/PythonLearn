# 方均根函数
# 注意啊！关键参数一定要在可变参数之前
# 也就是 RMS(f,*num) 正确
# RMS(*num,f)
def RMS(f,*num) :
    sum = 0 
    for n in num :
        sum += n*n
    sum /= len(num)
    return f(sum)

