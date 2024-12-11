"""
定义和使用字典

Version: 0.1
Author: jolie
Date: 2024-11-26
"""

#该函数执行了一系列字典操作。
def main():
    scores={'小猪':95,'小狗':88,'小猫':89}
    print(scores['小猪'])
    print(scores['小猫'])
    for j in scores:
        print('%s\t--->\t%d' % (j,scores[j]))
    scores['小狗']=96
    scores['小龟']=77
    scores.update(小鸭=99,小鹤=78) #使用 update 方法向字典 scores 中添加两个新的键值对：'小鸭' 与 99，'小鹤' 与 78。
    print(scores)
    if '小鸟' in scores:
        print(scores['小鸟'])
    print(scores.get('小鸟')) #使用 get 方法尝试获取 '小鸟' 的分数,，如果 '小鸟' 不在字典中，则返回 None。
    print(scores.get('小鸟',80))#使用 get 方法再次尝试获取 '小鸟' 的分数，如果 '小鸟' 不在字典中，则返回默认值 80。
    print(scores.popitem()) #使用 popitem 方法移除并返回字典中的一个键值对,由于字典是无序的，这将移除并返回最后一个添加的键值对，即 '小鹤' 与 78。
    print(scores.popitem()) #再次使用 popitem 方法移除并返回字典中的下一个键值对。
    print(scores.pop('小猪',100))#使用 pop 方法移除 '小猪' 并返回其值，如果 '小猪' 不存在，则返回默认值 100。
    print(scores.pop('小鹤',100))
    scores.clear() #使用 clear 方法清空字典 scores。
    print(scores)

if __name__ == '__main__':
    main()

# def main():
#     scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
#     print(scores['骆昊'])
#     print(scores['狄仁杰'])
#     for elem in scores:
#         print('%s\t--->\t%d' % (elem, scores[elem]))
#     scores['白元芳'] = 65
#     scores['诸葛王朗'] = 71
#     scores.update(冷面=67, 方启鹤=85)
#     print(scores)
#     if '武则天' in scores:
#         print(scores['武则天'])
#     print(scores.get('武则天'))
#     print(scores.get('武则天', 60))
#     print(scores.popitem())
#     print(scores.popitem())
#     print(scores.pop('骆昊', 100))
#     scores.clear()
#     print(scores)


# if __name__ == '__main__':
#     main()
