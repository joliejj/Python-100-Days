"""
生成斐波拉切数列

Version: 0.1
Author: joliej
Date: 2024-11-27
"""

def main():
    f=[1,1]
    for i in range(2,20):
        #f+=[f[i-1]+f[i-2]] #表达式 f+=[k] 是 Python 中向列表 f 追加元素 k的一种方式。这个表达式的含义是将k添加到列表 f 的末尾。
        f.append(f[i-1]+f[i-2])
    for j in f:
        print(j,end=' ')

if __name__=='__main__':
    main()

# def main():
#     f = [1 , 1]
#     for i in range(2, 20):
#         f += [f[i - 1] + f[i - 2]]
#         # f.append(f[i - 1] + f[i - 2])
#     for val in f:
#         print(val, end=' ')
#
#
# if __name__ == '__main__':
#     main()
