"""
输出斐波那契数列的前20个数
1 1 2 3 5 8 13 21 ...

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""

a = 1
b = 1
print(a,b,end=' ')
for _ in range(20):
    c=a + b
    a=b
    b=c
    print(c,end=' ')
    
