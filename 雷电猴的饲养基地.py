print("\n-----欢迎来到雷电猴的饲养基地-----")
print("版本V0.5.2")
ZT = 1
BBH = 'BT0.5.2'
choise = input("\n您要读档吗？（1.是  2.否）")
if (choise == '1'):
   with open('Bbh.data','r') as file:
         if file.read(7) == BBH:
            with open("ZT.data",'r') as file:
               ZT = file.read(1)
               print("----读档完成----")
               
         else:
             print("---读档失败---")
             if file.read() == '':
                print("对不起，未检测到您的存档")
                
               
             else:
                 print("不好意思，您的存档使用的是",file.read(),"版本或没有存档，无法被当前版本号", BBH,"所读取，请见谅")
elif (choise == '2'):
    choise2 = input("您确定嘛？(1.是 2.否)")
    if (choise2 == '1'):
       print("正在为您开启新游戏")
       print("开启成功！")
    if (choise2 == '2'):
      choise3 = input("那您到底要不要读档呀？(1.是)")
    if (choise3 == '1'):
       with open('Bbh.data','r') as file:
         if file.read(7) == BBH:
            with open("ZT.data",'r') as file:
               ZT = file.read(1)
               print("----读档完成----")
               
         else:
             print("---读档失败---")
             if file.read() == '':
                print("对不起，未检测到您的存档")
print("雷电猴已到达现场~")
print("更多功能正在抓紧制作中")
print('''Because English vertion not dnoe , so 
you can't set up English mode now ''')
print("因为英文版没有完成，所以你现在不能设置英文模式")
print("this is beta 0.5.2 vertion")
