"""
定义和使用矩形类

Version: 0.1
Author: jolie
Date: 2024-12-03
"""

class Rect(object):
    def __init__(self,width=0,height=0):
        #'初始化方法
        self.__width=width
        self.__height=height

    def perimeter(self):
        #'计算周长'
        return (self.__width+self.__width)*2

    def area(self):
        #计算面积
        return (self.__width*self.__height)

    def __str__(self):
        return '矩形 %.1f,%.1f'%(self.__width,self.__height)

    def __del__(self):
        """析构器"""
        print('销毁矩形对象')

if __name__ == '__main__':
    rect1=Rect()
    print(rect1)
    print(rect1.perimeter())
    print(rect1.area())
    rect2 = Rect(3.5, 4.5)
    print(rect2)
    print(rect2.perimeter())
    print(rect2.area())
