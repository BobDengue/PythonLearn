# coding = ' UTF-8 '
# ax2 + bx + c = 0
import math
def solutionToEquation(a,b,c) : 
    if not( isinstance(a,(int,float)) and isinstance(b,(int,float)) 
    and isinstance(c,(int,float))) :
        raise TypeError('bad operand type')
    delta = b*b - 4*a*c 
    if delta < 0 :
        print('No real root')
        return 
    delta_sqrt = math.sqrt(delta)
    root1 = (-b + delta_sqrt)/2/a
    root2 = (-b - delta_sqrt)/2/a
    return root1,root2