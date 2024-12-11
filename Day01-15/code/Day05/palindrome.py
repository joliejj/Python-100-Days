"""
判断输入的正整数是不是回文数
回文数是指将一个正整数从左往右排列和从右往左排列值一样的数

Version: 0.1
Author: joliej
Date: 2024-11-20
"""


a=int(input("请输入一个正整数："))
temp=a
b=[]
i=0
while(temp>0):
    b.append(temp%10)
    temp=int(temp/10)
    print(temp,end=' ')
    i=i+1
c=0
print(b,end=' ')
print("i=%d"%i)
for j in range(i):
    c=c*10+b[j]

if a == c:
    print('%d是回文数' % a)
else:
    print('%d不是回文数' % a)