"""
找出1~9999之间的所有完美数
完美数是除自身外其他所有因子的和正好等于这个数本身的数
例如: 6 = 1 + 2 + 3, 28 = 1 + 2 + 4 + 7 + 14

Version: 0.1
Author: joliej
Date: 2024-11-20
"""
import math

for num in range(2,10000):
    result=0
    #fw=int(math.sqrt(num))
    temp=[]
    for factor in range(1,num):
        if num % factor ==0:
            result+=factor
            temp.append(factor)
    
           # if factor>1 and num//factor!=factor:
            #    result+=factor
           #     temp.append(factor)
    if result ==num and len(temp)>1:
        print(num,'=')
        for i in temp:
            print(i,end='+')
        print()
