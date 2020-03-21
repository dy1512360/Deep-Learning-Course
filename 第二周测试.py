import math
a = float(input("请输入a的值："))
b = float(input("请输入b的值："))
c = float(input("请输入c的值："))
d = (b**2)-(4*a*c)
if d > 0:
    print('此时方程有两个解')
    bb1 = (-b+math.sqrt(d))/(a*2)
    bb2 = (-b-math.sqrt(d))/(a*2)
    print("x1=",bb1,"\t","x2=",bb2)
elif d==0:
    print('此时方程有一个解')
    bb1 = (-b+math.sqrt(d))/(a*2)
    print("x1=",bb1,"\t")
elif d<0:
    print('此时方程无解')

