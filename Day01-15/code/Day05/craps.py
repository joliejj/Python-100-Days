"""
Craps赌博游戏
玩家摇两颗色子 如果第一次摇出7点或11点 玩家胜
如果摇出2点 3点 12点 庄家胜 其他情况游戏继续
玩家再次要色子 如果摇出7点 庄家胜
如果摇出第一次摇的点数 玩家胜
否则游戏继续 玩家继续摇色子
玩家进入游戏时有1000元的赌注 全部输光游戏结束

Version: 0.1
Author: 骆昊
Date: 2018-03-02
"""


from random import randint
money=1000
while(money>0):
    print("你的总资产为%d"%money)
    will=input("还玩吗？Y/N")
    if will=="Y" or will=="y":
        debt=int(input("请下注:"))
        if debt>money:
            print("钱不够了！")
        elif debt<0:
            print("请输入正整数")
        else:
            go_on=True
        
        while go_on:
            a0=randint(1,6)
            b0=randint(1,6)
            first1=a0+b0
            print("玩家第一局掷出了%d点"%first1)
            if first1==7 or first1==11:
                print("玩家胜")
                money+=debt
                go_on=False
            elif first1==2 or first1==3 or first1==12:
                print("玩家输")
                money-=debt
                go_on=False
            else:
                a2=randint(1,6)
                b2=randint(1,6)
                second2=a2+b2
                if second2==7:
                    print("玩家输")
                    money-=debt
                    go_on=False
                elif second2==first1:
                    print("玩家胜")
                    money+=debt
                    go_on=False
    else:
        printf ("你不玩了，你带走了%d的钱"%money)
printf("你亏光了")
                

