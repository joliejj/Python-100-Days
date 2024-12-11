"""
生成列表
- 用range创建数字列表
- 生成表达式
- 生成器

Version: 0.1
Author: joliej
Date: 2024-11-27
"""

#fibonacci序列的生成器
def fib(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
        yield a

def main():
    n=int(input('请输入数字：'))
    list1=list(range(1,n))
    print(list1)
    list2=[x*x for x in range(1,n)]
    print(list2)
    list3=[i+j for i in 'ABCDEFG' for j in '12345']
    print(list3)
    print(len(list3))
    list4=(i+j for i in 'ABCDEFG' for j in '12345')
    print(list4)
    for elem in list4:
        print(elem,end=' ')
    print()
    list4=fib(20)
    print(list4)
    for elem in list4:
        print(elem,end=' ')
    print()


if __name__ == '__main__':
    main()

# def main():
#     # 用range创建数值列表
#     list1 = list(range(1, 11))
#     print(list1)
#     # 生成表达式
#     list2 = [x * x for x in range(1, 11)]
#     print(list2)
#     list3 = [m + n for m in 'ABCDEFG' for n in '12345']
#     print(list3)
#     print(len(list3))
#     # 生成器(节省空间但生成下一个元素时需要花费时间)
#     gen = (m + n for m in 'ABCDEFG' for n in '12345')
#     print(gen)
#     for elem in gen:
#         print(elem, end=' ')
#     print()
#     gen = fib(20)
#     print(gen)
#     for elem in gen:
#         print(elem, end=' ')
#     print()


