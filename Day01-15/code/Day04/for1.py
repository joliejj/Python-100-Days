"""
用for循环实现1~100求和

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""

sum = 0
for x in range(1, 101): #range(a,b)的取值默认从a到b-1
    sum += x
print(sum)
