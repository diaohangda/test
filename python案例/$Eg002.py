"""
    实例002：“个税计算”
    题目 企业发放的奖金根据利润提成。利润
    (I)低于或等于10万元时，奖金可提10%；
    (2)利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
    (3)20万到40万之间时，高于20万元的部分，可提成5%；
    (4)40万到60万之间时，高于40万元的部分，可提成3%；
    (5)60万到100万之间时，高于60万元的部分，可提成1.5%;
    (6)高于100万元时，超过100万元的部分按1%提成.
    从键盘输入当月利润I，求应发放奖金总数？

    程序分析 分区间计算即可。
"""

kaiguan=True

money=[100000,100000,200000,200000,400000]
ticheng=[0.1,0.075,0.05,0.03,0.015,0.01]
while kaiguan:
    memor_sum = 0
    print('\n退出请输入q')
    User_money=input('请输入当月利润：')
    if User_money=='q':
        break
    User_input=int(User_money)
    for i in range(len(money)):
        if User_input<=money[i]:
            memor_sum+=User_input*ticheng[i]
            User_input=0
            break
        else:
            memor_sum+=money[i]*ticheng[i]
            User_input-=money[i]

    memor_sum+=User_input*money[-1]
    print(memor_sum)

