"""
用for循环实现1~100之间的偶数求和

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""

sum = 0
for x in range(2, 101, 2): #range(a,b,c)从a开始，到b-1结束，以步长c增加
    sum += x
print(sum)
