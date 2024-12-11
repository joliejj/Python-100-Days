"""
列表常用操作
- 列表连接
- 获取长度
- 遍历列表
- 列表切片
- 列表排序
- 列表反转
- 查找元素

Version: 0.1
Author: joliej
Date: 2024-11-27
"""

def main():
    fruits=['grape','apple','strawberry','waxberry']
    fruits+=['pitaya','pear','mango']
    for fruit in fruits:
        print(fruit.title(),end=',')
    print()

    fruits2=fruits[1:5]
    print(fruits2)
    fruits3=fruits[0:5]
    print(fruits3)
    fruits4=fruits[-4:-2]#使用切片操作创建一个新的列表 fruits4，包含 fruits 列表中倒数第四个到倒数第三个元素。
    print(fruits4)
    fruits5=fruits[::-1]
    print(fruits5)


if __name__ == '__main__':
    main()
