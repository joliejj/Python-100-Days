"""
字典的常用操作

Version: 0.1
Author: jolie
Date: 2024-11-27
"""
def main():
    stu={'name':'小猪','age':38,'gender':True}
    print(stu)
    print(stu.keys())
    print(stu.values())
    print(stu.items())
    for j in stu.items():
        print(j)
        print(j[0],j[1])
    if 'age' in stu:
        stu['age']=30
    print(stu)
    stu.setdefault('score',80) #使用 setdefault 方法为字典 stu 设置默认值，如果 'score' 不存在，则添加 'score' 键并赋值为 80。
    print(stu)
    stu.setdefault('score',100)#再次使用 setdefault 方法尝试为字典 stu 设置默认值，由于 'score' 已存在，所以不会改变其值。
    print(stu)
    stu['score']=110
    print(stu)

if __name__ == '__main__':
    main()

# def main():
#     stu = {'name': '骆昊', 'age': 38, 'gender': True}
#     print(stu)
#     print(stu.keys())
#     print(stu.values())
#     print(stu.items())
#     for elem in stu.items():
#         print(elem)
#         print(elem[0], elem[1])
#     if 'age' in stu:
#         stu['age'] = 20
#     print(stu)
#     stu.setdefault('score', 60)
#     print(stu)
#     stu.setdefault('score', 100)
#     print(stu)
#     stu['score'] = 100
#     print(stu)
#
#
# if __name__ == '__main__':
#     main()
