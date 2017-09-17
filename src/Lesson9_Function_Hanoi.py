# This program aims to achieve the hanoi problem
# It consists of three rods and a number of disks of different sizes, 
# which can slide onto any rod. 
# The puzzle starts with the disks in a neat stack in ascending order of size on one rod,
# the smallest at the top, thus making a conical shape.
# []                     | 
# [ ]                    |
# [  ]                   |
# ....                   |  
# [    ]                 | n      
# A         B        C
# transfer disc on rod A to rod C by rod B
def Hanoi(n,a='A',b='B',c='C'):
    if n==1 :
        print('move',a,'-->',c)
        return 
    Hanoi(n-1,a,c,b)
    print('move',a,'-->',c)
    Hanoi(n-1,b,a,c)