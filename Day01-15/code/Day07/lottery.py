"""
双色球随机选号程序

Version: 0.1
Author: joliej
Date: 2024-11-28
"""

from random import randrange, randint, sample




def display(balls):
    "定义了一个名为 display 的函数，它接受一个参数 balls，这个参数是一个列表，包含了双色球的号码。"
    "输出列表中的双色球号码"
    for index,ball in enumerate(balls):
        #使用 enumerate 函数遍历 balls 列表,同时获取每个元素的索引 index 和值 ball
        if index==len(balls)-1:#如果当前元素是列表中的最后一个元素，则打印一个竖线 '|'。
            print('|',end=' ')
        print('%02d'%ball,end=' ')#对于每个球号码，使用 %02d 格式化字符串确保号码以两位数的形式打印（例如 '01'，'02' 等）
    print()

def random_select():
    "定义了一个名为 random_select 的函数，用于随机选择一组双色球号码"
    red_balls=[x for x in range(1,34)] #从范围生成数字列表：生成一个包含1到33的数字列表red_balls
    print(red_balls)
    print()
    for index, ball in enumerate(red_balls):
        print(f'red_balls[{index}]={red_balls[index]}', end=' ')
    print()
    selected_balls=[]#初始化一个空列表 selected_balls 用于存储选中的号码。
    for i in range(6):
        #在双色球游戏中，需要从33个红球中选择6个号码。range(6) 生成的序列确保循环正好执行6次，对应于双色球游戏中需要选择的6个红球号码。
        index=randrange(len(red_balls))#使用 randrange 函数生成一个随机索引，然后从 red_balls 列表中选择对应的号码
        #randrange() 函数是 random 模块中的一个函数，用于生成一个指定范围内的随机整数。
        #print(f'index='{index},end=' ')
        print(f'red_balls[{index}]={red_balls[index]}',end=' ')
        #每次选择和删除操作都会改变 red_balls 列表，因此后续选择的索引与初始列表中的索引不同。
        selected_balls.append(red_balls[index])#将从 red_balls 列表中选择对应的号码,添加到 selected_balls 列表中。
        del red_balls[index] #从 red_balls 列表中删除已选的号码，以确保不会有重复的号码被选中。
    print()
    selected_balls.sort()
    selected_balls.append(randint(1,16))
    return selected_balls

def main():
    n=int(input('随机选几注：'))
    for j in range(n):
        display(random_select())

if __name__ == '__main__':
    main()

# def display(balls):
#     """
#     输出列表中的双色球号码
#     """
#     for index, ball in enumerate(balls):
#         if index == len(balls) - 1:
#             print('|', end=' ')
#         print('%02d' % ball, end=' ')
#     print()
#
# def random_select():
#     """
#     随机选择一组号码
#     """
#     red_balls = [x for x in range(1, 34)]
#     selected_balls = []
#     for _ in range(6):
#         index = randrange(len(red_balls))
#         selected_balls.append(red_balls[index])
#         del red_balls[index]
#     # 上面的for循环也可以写成下面这行代码
#     # sample函数是random模块下的函数
#     # selected_balls = sample(red_balls, 6)
#     selected_balls.sort()
#     selected_balls.append(randint(1, 16))
#     return selected_balls
#
#
# def main():
#     n = int(input('机选几注: '))
#     for _ in range(n):
#         display(random_select())
#
#
# if __name__ == '__main__':
#     main()
