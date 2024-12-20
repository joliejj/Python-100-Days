"""
输入学生考试成绩计算平均分

Version: 0.1
Author: jolie
Date: 2024-11-26
"""


def main():
    number = int(input('请输入学生人数: '))
    names = [None] * number
    scores = [None] * number
    for index in range(len(scores)):
        names[index] = input('请输入第%d个学生的名字：' % (index + 1))
        scores[index] = float(input('请输入第%d个学生的成绩: ' % (index + 1)))
    total = 0
    for index in range(len(scores)):
        print('%s %.1f分'% (names[index], scores[index]))
        total += scores[index]
    print('平均成绩是: %.1f分' % (total / number))


if __name__ == '__main__':
    main()
