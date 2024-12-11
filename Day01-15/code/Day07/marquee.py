"""
用于在终端或命令行界面上实现一个滚动文本的效果

Version: 0.1
Author: jolie
Date: 2024-11-28
"""

import os
import time


def main():
    str = 'Welcome to China to have delicious food'
    while True:
        print(str)
        time.sleep(0.3) #使用 time.sleep(0.2) 暂停0.2秒
        str = str[1:] + str[0:1]
        #字符串 str 被重新赋值为其自身的第二个字符到最后一个字符（str[1:]），再加上它的第一个字符（str[0:1]）。
        # 这个操作实际上是将字符串的第一个字符移动到了字符串的末尾，实现了一个字符的滚动效果。
        # for Windows use os.system('cls') instead
        #os.system('clear')#在打印新的字符串之前，使用 os.system('clear') 清除当前终端的屏幕。
        os.system('cls')#在Windows系统上运行，应该使用 os.system('cls') 来清除屏幕。
        # 这个命令的作用是清除屏幕上之前的输出，使得滚动效果更加连贯。

if __name__ == '__main__':
    main()
