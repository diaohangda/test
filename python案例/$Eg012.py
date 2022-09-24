"""
    实例013：所有水仙花数
    题目 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。
    例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。

    程序分析 利用for循环控制100-999个数，每个数分解出个位，十位，百位。
"""
for i in range(100,1000):
    s=str(i)
    one=int(s[-1])
    ten=int(s[-2])
    hun=int(s[-3])
    if i == one**3+ten**3+hun**3:
        print(i)

# for i in range(100,1000):
#     one=int(i/100)
#     two=int((i/10)%10)
#     three=int((i%100)%10)
#     if i == one**3+two**3+three**3:
#         print(i)