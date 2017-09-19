# def Triangles( degreeOfAngle=6) :
#     counter = 1
#     angleList = [1]      
#     if counter == degreeOfAngle :
#         return
#     angleList.
#     counter += 1 
#     yield 

# from baidu baike
def Triangles() :
    L = [1] 
    while True :
        yield L
        L.append(0)
        L=[ L[i-1] + L[i] for i in range(len(L))]

# L[-1] = 0 
# 因为每次 append(0) 