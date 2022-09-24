"""
    实例020：高空抛物
    题目 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，
    共经过多少米？第10次反弹多高？
"""

high=100
meter=0
count=0
for i in range(10):
    meter+=high
    high/=2
    count+=1
    print('现在高度:',high)
    print('次数：',count)
    print('经过多少米:',meter)
    print()


# high=200.
# total=100
# for i in range(10):
#     high/=2
#     total+=high
#     print(high/2)
# print('总长：',total)

