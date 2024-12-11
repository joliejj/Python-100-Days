"""
定义和使用时钟类

Version: 0.1
Author: 骆昊
Date: 2018-03-08
"""

import time
import os
#在 Python 中，当你使用 time 模块的 localtime() 或 gmtime() 函数时，
#它们会返回一个 struct tm 类型的对象（在 Python 中表现为元组），
#这个对象包含了当前本地时间或世界协调时间（UTC）的详细信息

class Clock(object):

    # Python中的函数是没有重载的概念的
    # 因为Python中函数的参数没有类型而且支持缺省参数和可变参数
    # 用关键字参数让构造器可以传入任意多个参数来实现其他语言中的构造器重载
    def __init__(self,**kw):
        #构造器会检查这个字典中是否包含hour、minute和second键，如果包含，就使用这些值来设置时钟的时间
        if 'hour' in kw and 'minute' in kw and 'second' in kw:
            self._hour=kw['hour']
            self._minute=kw['minute']
            self._second=kw['second']
        else:
            tm=time.localtime(time.time())
            # time.time()函数用于获取当前时间的时间戳
            # time.localtime()函数接受一个时间戳（可以是time.time()返回的值）作为参数，
            # 并将其转换为表示本地时间的struct tm对象。
            # 这个对象包含了年、月、日、小时、分钟、秒等信息，
            # 具体成员包括tm_year、tm_mon、tm_mday、tm_hour、tm_min、tm_sec等。
            self._hour=tm.tm_hour
            self._minute=tm.tm_min
            self._second=tm.tm_sec

    def run(self):
        self._second+=1
        if self._second==60:
            self._second=0
            self._minute+=1
            if self._minute==60:
                self._minute=0
                self._hour+=1
                if self._hour==24:
                    self._hour=0


    def show(self):
        return '%02d:%02d:%02d' % (self._hour, self._minute, self._second)

if __name__ =='__main__':
    # kw 是一个字典 {'hour': 10, 'minute': 5, 'second': 58}。
    clock= Clock(hour=10,minute=5,second=56)
    # clock = Clock()
    while True:
        os.system('cls')#使用 os.system('cls') 来清除屏幕。
        print(clock.show())
        time.sleep(1)#time.sleep(1) 用于在每次循环中暂停程序1秒钟，以模拟时钟的秒针移动。
        clock.run()
