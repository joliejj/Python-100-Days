"""
输入两个正整数计算最大公约数和最小公倍数

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""

x = int(input('x='))
y=int(input('y='))
if x>y:
    (x,y)=(y,x)
for _ in range(x,0,-1):
    if x % _ ==0 and y % _==0:
        print('%d和%d的最大公约数为%d'%(x,y,_))
        print('%d和%d的最小公倍数为%d'%(x,y,x*y/_))
        break
