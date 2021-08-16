print("\n-----欢迎来到雷电猴的饲养基地-----")
print("版本V0.5.5")
ZT = 1
BBH = 'BT0.5.5'
choise = input("\n您要读档吗？（1.是  2.否）")
if (choise == '1'):
    with open('Bbh.data', 'w+') as file:
        if file.read(7) == BBH:
            file.close()
            with open("ZT.data", 'r') as file:
                ZT = file.read(1)
                file.close()
                print("----读档完成----")

        else:
            print("---读档失败---")
            if file.read() == '':
                print("对不起，未检测到您的存档，或者版本号过低")
                print("正在开启新游戏并为您更新存档")
                file.write(BBH)
                file.close()
elif (choise == '2'):
    choise2 = input("您确定嘛？(1.是 2.否)")
    if (choise2 == '1'):
        print("正在为您开启新游戏")
        print("开启成功！")
    elif (choise2 == '2'):
        choise3 = input("那您到底要不要读档呀？(1.是)")
        if (choise3 == '1'):
            with open('Bbh.data', 'r') as file:
                if file.read(7) == BBH:
                    file.close()
                    with open("ZT.data", 'r') as file:
                        ZT = file.read(1)
                        file.close()
                        print("----读档完成----")

                else:
                    print("---读档失败---")
                    if file.read(7) == '':
                        file.close()
                        print("对不起，未检测到您的存档，或者版本号过低")
                        print("正在开启新游戏并为您更新存档")
                        with open('Bbh.data', 'r+') as file:
                            file.write(BBH)
                            file.close()
print("雷电猴已到达现场~")
choise4 = input("您要执行什么操作？\n1.指令列表\n2.存档\n3.输入指令")
if (choise4 == '1'):
    print('''---指令列表---
\n喂食\nfeed.l\n商店\nshop.l\n存档\narchive.l''')
elif (choise4 == '2'):
    jd = input("请输入指令")
    if (jd == 'archive.l'):
        with open('ZT.data', 'r+') as file:
            file.write(ZT)
            file.close()
        print("存档成功！")
    else:
        print("错误！")


elif (choise4 == '3'):
    jd2 = input("请输入指令")
    if (jd2 == "feed.l"):
        print("喂食成功！饱食度+1")
    elif (jd2 == "shop.l"):
        print("====商店====\n暂时没有东西")
    elif (jd2 == "archive.l"):
        with open('ZT.data', 'r+') as file:
            file.write(ZT)
            file.close()
        print("存档成功！")
    else:
        print("错误！")


print('''Because English vertion not dnoe , so 
you can't set up English mode now ''')
print("因为英文版没有完成，所以你现在不能设置英文模式")
