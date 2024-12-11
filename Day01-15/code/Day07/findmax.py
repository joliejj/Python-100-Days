"""
找出列表中最大或最小的元素

Version: 0.1
Author: joliej
Date: 2024-11-27
"""

def main():
    fruits=['grape','apple','apple','strawberry','waxberry','pitaya']
    max_value=min_value= fruits[0]
    for i in range(1,len(fruits)):
        if fruits[i]>max_value:
            max_value=fruits[i]
        elif fruits[i]<min_value:
            min_value=fruits[i]
    print('max',max_value)
    print('min',min_value)

if __name__=='__main__':
    main()

# def main():
#     fruits = ['grape', 'apple', 'strawberry', 'waxberry', 'pitaya']
#     # 直接使用内置的max和min函数找出列表中最大和最小元素
#     # print(max(fruits))
#     # print(min(fruits))
#     max_value = min_value = fruits[0]
#     for index in range(1, len(fruits)):
#         if fruits[index] > max_value:
#             max_value = fruits[index]
#         elif fruits[index] < min_value:
#             min_value = fruits[index]
#     print('Max:', max_value)
#     print('Min:', min_value)
#
#
# if __name__ == '__main__':
#     main()
# 想一想如果最大的元素有两个要找出第二大的又该怎么做 
