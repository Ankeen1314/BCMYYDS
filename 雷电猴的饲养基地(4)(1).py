print("\n-----欢迎来到雷电猴的饲养基地-----")
print("版本V0.5.5")
状态 = 1
VERSION = '0.5.5'
choise = input("\n您要读档吗？（1.是  2.否）")


def func_读档():
    with open("VERSION.data", 'w+', encoding='utf-8') as file:
        if file.read() == VERSION:
            file.close()
            with open("ZT.data", 'w+', encoding='utf-8') as file2:
                状态 = file2.read()
                print("----读档完成----")
        else:
            print("---读档失败---")
            if file.read() == "":
                print("对不起，未检测到您的存档，或者版本号过低")
                print("正在开启新游戏并为您更新存档")
                file.write(str(VERSION))


if (choise == '1'):
    func_读档()

elif (choise == '2'):

    choise = input("您确定嘛？(1.是 2.否)")
    if (choise == '1'):
        print("正在为您开启新游戏")
        print("开启成功！")
    elif (choise == '2'):
        choise = input("那您到底要不要读档呀？(1.是)")
        if (choise == '1'):
            func_读档()

print("雷电猴已到达现场~")
choise = input("""您要执行什么操作？
1.指令列表
2.存档
3.输入指令""")

if (choise == '1'):
    print('''---指令列表---
喂食
feed.l
商店
shop.l
存档
archive.l''')

elif (choise == '2'):
    jd = input("请输入指令")
    if (jd == 'archive.l'):
        with open('ZT.data', 'w', encoding='utf-8') as file:
            file.write(str(状态))
            file.close()
        print("存档成功")
    else:
        print("错误！")

elif (choise == '3'):
    jd2 = input("请输入指令")
    if (jd2 == "feed.l"):
        print("喂食成功！饱食度+1")
    elif (jd2 == "shop.l"):
        print("====商店====\n暂时没有东西")
    elif (jd2 == "archive.l"):
        with open('ZT.data', 'w', encoding='utf-8') as file:
            file.write(str(状态))
            file.close()
        print("存档成功！")
    else:
        print("错误！")


print('''Because English vertion not dnoe , so 
you can't set up English mode now ''')
print("因为英文版没有完成，所以你现在不能设置英文模式")
