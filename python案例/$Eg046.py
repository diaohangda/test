"""
    实例081：求未知数
    题目 809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，
         8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，及809*??后的结果。

    程序分析 无。
"""
a=809
for i in range(10,100):
    if a*i==800*i+9*i and 10<=8*i<100 and 100<=9*i<1000:
        print(i)
        print('809*'+str(i)+'='+str(a*i))


# a = 809
# for i in range(10,100):
#     b = i * a
#     if b >= 1000 and b <= 10000 and 8 * i < 100 and 9 * i >= 100:
#         print(b,' = 800 * ', i, ' + 9 * ', i)
#
# for i in range(10,100):
#     if 8*i>99 or 9*i<100:
#         continue
#     if 809*i==800*i+9*i:
#         print(i)
#         break
